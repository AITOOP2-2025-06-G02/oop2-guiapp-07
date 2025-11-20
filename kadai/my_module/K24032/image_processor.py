"""画像合成処理モジュール

このモジュールは、撮影画像と背景画像（google.png）を合成する機能を提供します。
白色ピクセルをカメラ撮影画像で置き換えるクロマキー合成を実装しています。

Author: K24032 大石大雅
"""

import numpy as np
import cv2
from typing import Optional


class ImageProcessor:
    """画像合成処理を行うクラス"""

    def __init__(self):
        """画像プロセッサを初期化"""
        self.base_image: Optional[cv2.Mat] = None
        self.captured_image: Optional[cv2.Mat] = None
        self.result_image: Optional[cv2.Mat] = None

    def load_base_image(self, filepath: str) -> bool:
        """背景画像（google.png）を読み込む

        Args:
            filepath (str): 背景画像のファイルパス

        Returns:
            bool: 読み込み成功時True、失敗時False
        """
        self.base_image = cv2.imread(filepath)
        if self.base_image is None:
            return False
        return True

    def set_captured_image(self, image: cv2.Mat) -> None:
        """撮影画像をセットする

        Args:
            image (cv2.Mat): カメラで撮影した画像
        """
        self.captured_image = image.copy()

    def compose_images(self) -> bool:
        """画像合成を実行する

        背景画像の白色部分（RGB: 255, 255, 255）を撮影画像で置き換える。
        撮影画像がベース画像より小さい場合はタイル状に繰り返して配置。

        Returns:
            bool: 合成成功時True、失敗時False
        """
        if self.base_image is None or self.captured_image is None:
            return False

        # 背景画像をコピー（元の画像を保持）
        result = self.base_image.copy()

        # 画像サイズを取得
        b_height, b_width, _ = self.base_image.shape
        c_height, c_width, _ = self.captured_image.shape

        # ピクセルごとに処理
        for y in range(b_height):
            for x in range(b_width):
                b, g, r = result[y, x]
                # 白色ピクセルを撮影画像で置き換え
                if (b, g, r) == (255, 255, 255):
                    # タイル状に配置（%演算で繰り返し）
                    result[y, x] = self.captured_image[y % c_height, x % c_width]

        self.result_image = result
        return True

    def save_result(self, filepath: str) -> bool:
        """合成結果を保存する

        Args:
            filepath (str): 保存先のファイルパス

        Returns:
            bool: 保存成功時True、失敗時False
        """
        if self.result_image is None:
            return False

        return cv2.imwrite(filepath, self.result_image)

    def get_result_image(self) -> Optional[cv2.Mat]:
        """合成結果画像を取得する

        Returns:
            Optional[cv2.Mat]: 合成結果画像。未合成の場合はNone
        """
        return self.result_image
