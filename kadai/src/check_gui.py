# check_gui.py
"""画像合成カメラGUIアプリケーション

Author: K24032 大石大雅（ビューとモデルのインターフェース開発担当）
"""

import sys
import os
import cv2
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QImage, QPixmap
from ui_mainwindow import Ui_MainWindow

# パスの設定（kadai/src/ から実行されることを想定）
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from my_module.K24139.lecture05_camera_image_capture import MyVideoCapture
from my_module.K24032.image_processor import ImageProcessor


class ImageProcessorApp(QMainWindow):
    """画像処理GUIアプリケーションのメインクラス"""

    def __init__(self):
        super().__init__()
        # デザインを適用
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # モデルの初期化
        self.camera = None
        self.image_processor = ImageProcessor()
        self.captured_image = None
        self.is_camera_active = False

        # タイマーの初期化（カメラプレビュー用）
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_camera_feed)

        # ボタンのイベント接続
        self.ui.btn_capture.clicked.connect(self.on_capture_and_compose)
        self.ui.btn_save.clicked.connect(self.on_save_image)

        # 初期状態の設定
        self.ui.btn_save.setEnabled(False)
        self.update_status("準備完了：撮影ボタンを押してください")

        # カメラの初期化
        self.initialize_camera()

    def initialize_camera(self):
        """カメラを初期化してプレビューを開始"""
        try:
            self.camera = MyVideoCapture()
            self.is_camera_active = True
            self.timer.start(30)  # 30msごとに更新（約30fps）
            self.update_status("カメラ準備完了：撮影ボタンを押してください")
        except Exception as e:
            self.update_status(f"カメラ接続エラー: {str(e)}")
            self.ui.btn_capture.setEnabled(False)

    def update_camera_feed(self):
        """カメラ映像をリアルタイムで表示"""
        if not self.is_camera_active or self.camera is None:
            return

        frame = self.camera.capture_frame()
        if frame is None:
            return

        # ターゲットマークを描画
        frame_with_mark = self.camera.draw_target_mark(frame.copy())
        # 左右反転
        frame_with_mark = cv2.flip(frame_with_mark, 1)

        # QPixmapに変換して表示
        self.display_image(frame_with_mark, self.ui.lbl_camera_feed)

    def on_capture_and_compose(self):
        """撮影・合成ボタンが押されたときの処理"""
        if not self.is_camera_active or self.camera is None:
            self.update_status("カメラが利用できません")
            return

        # 現在のフレームを撮影
        frame = self.camera.capture_frame()
        if frame is None:
            self.update_status("撮影に失敗しました")
            return

        self.captured_image = frame
        self.update_status("撮影完了！合成処理を開始します...")

        # カメラプレビューを停止
        self.timer.stop()
        self.is_camera_active = False

        # 撮影画像を保存
        os.makedirs('../images', exist_ok=True)
        cv2.imwrite('../images/camera_capture.png', self.captured_image)

        # 画像合成処理
        self.compose_image()

    def compose_image(self):
        """画像合成を実行"""
        # 背景画像を読み込み
        base_image_path = '../images/google.png'
        if not os.path.exists(base_image_path):
            self.update_status(f"エラー: {base_image_path} が見つかりません")
            return

        # 画像プロセッサで合成
        self.image_processor.load_base_image(base_image_path)
        self.image_processor.set_captured_image(self.captured_image)

        if self.image_processor.compose_images():
            # 合成結果を表示
            result = self.image_processor.get_result_image()
            self.display_image(result, self.ui.lbl_result_image)

            # 自動保存
            os.makedirs('../output_images', exist_ok=True)
            save_path = '../output_images/lecture05_01_k24032.png'
            if self.image_processor.save_result(save_path):
                self.update_status(f"画像合成完了！保存先: {save_path}")
                self.ui.btn_save.setEnabled(True)
            else:
                self.update_status("合成は成功しましたが、自動保存に失敗しました")
        else:
            self.update_status("画像合成に失敗しました")

    def on_save_image(self):
        """保存ボタンが押されたときの処理（別名保存）"""
        if self.image_processor.get_result_image() is None:
            self.update_status("保存する画像がありません")
            return

        # ファイルダイアログで保存先を選択
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "画像を保存",
            "../output_images/lecture05_01_k24032.png",
            "画像ファイル (*.png *.jpg *.jpeg)"
        )

        if file_path:
            if self.image_processor.save_result(file_path):
                self.update_status(f"画像を保存しました: {file_path}")
            else:
                self.update_status("画像の保存に失敗しました")

    def display_image(self, cv_image, label):
        """OpenCV画像をQtラベルに表示

        Args:
            cv_image: OpenCV形式の画像（BGR）
            label: 表示先のQLabelウィジェット
        """
        # BGRからRGBに変換
        rgb_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w

        # QImageに変換
        qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        # QPixmapに変換してラベルにセット
        pixmap = QPixmap.fromImage(qt_image)
        # ラベルのサイズに合わせて拡大縮小（アスペクト比維持）
        scaled_pixmap = pixmap.scaled(
            label.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        label.setPixmap(scaled_pixmap)

    def update_status(self, message):
        """ステータスメッセージを更新

        Args:
            message (str): 表示するメッセージ
        """
        self.ui.lbl_status.setText(f"📌 {message}")
        self.ui.statusbar.showMessage(message)

    def closeEvent(self, event):
        """ウィンドウを閉じるときの処理"""
        if self.camera is not None:
            self.timer.stop()
            del self.camera
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageProcessorApp()
    window.show()
    sys.exit(app.exec())