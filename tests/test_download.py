from __future__ import annotations

from unittest import IsolatedAsyncioTestCase

from parameterized import parameterized

from tts import API_KEY, BASE_URL, Tts
from tts.errors.files import MakeException

# TODO: 出来ればアクセスしたくないけどエラーモックめんどくさい


class TestDownload(IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        self.tts = Tts(BASE_URL, API_KEY)

    async def asyncTearDown(self) -> None:
        del self.tts

    @parameterized.expand(
        [
            ("show", "happiness", 2, 100, 100),
            ("haruka", "happiness", 2, 100, 100),
            ("hikari", "happiness", 2, 100, 100),
            ("takeru", "happiness", 2, 100, 100),
            ("santa", "happiness", 2, 100, 100),
            ("bear", "happiness", 2, 100, 100),
        ]
    )
    async def test_success_speaker(self, speaker, emotion, emotion_lvl, pitch, speed):
        result = await self.tts.download_voice_byte(
            "test",
            speaker=speaker,
            emotion=emotion,
            emotion_level=emotion_lvl,
            pitch=pitch,
            speed=speed,
        )

        self.assertIsNotNone(result)

    @parameterized.expand(
        [
            ("haruka", "happiness", 2, 100, 100),
            ("haruka", "anger", 2, 100, 100),
            ("haruka", "sadness", 2, 100, 100),
        ]
    )
    async def test_success_emotion(self, speaker, emotion, emotion_lvl, pitch, speed):
        result = await self.tts.download_voice_byte(
            "test",
            speaker=speaker,
            emotion=emotion,
            emotion_level=emotion_lvl,
            pitch=pitch,
            speed=speed,
        )

        self.assertIsNotNone(result)

    @parameterized.expand(
        [
            ("haruka", "happiness", 1, 100, 100),
            ("haruka", "happiness", 2, 100, 100),
            ("hikari", "happiness", 3, 100, 100),
            ("hikari", "happiness", 4, 100, 100),
        ]
    )
    async def test_success_emotion_level(
        self, speaker, emotion, emotion_lvl, pitch, speed
    ):
        result = await self.tts.download_voice_byte(
            "test",
            speaker=speaker,
            emotion=emotion,
            emotion_level=emotion_lvl,
            pitch=pitch,
            speed=speed,
        )

        self.assertIsNotNone(result)

    @parameterized.expand(
        [(50, "haruka", "happiness", 1, 200), (200, "haruka", "happiness", 1, 200)]
    )
    async def test_success_pitch(self, pitch, speaker, emotion, emotion_lvl, speed):
        result = await self.tts.download_voice_byte(
            "test",
            speaker=speaker,
            emotion=emotion,
            emotion_level=emotion_lvl,
            pitch=pitch,
            speed=speed,
        )
        self.assertIsNotNone(result)

    @parameterized.expand([("dummy", "happiness", 1, 200, 200)])
    async def test_failed_speaker(self, speaker, emotion, emotion_lvl, pitch, speed):
        with self.assertRaises(MakeException):
            await self.tts.download_voice_byte(
                "test",
                speaker=speaker,
                emotion=emotion,
                emotion_level=emotion_lvl,
                pitch=pitch,
                speed=speed,
            )

    @parameterized.expand([("haruka", "dummy", 1, 200, 200)])
    async def test_failed_emotion(self, speaker, emotion, emotion_lvl, pitch, speed):
        with self.assertRaises(MakeException):
            await self.tts.download_voice_byte(
                "test",
                speaker=speaker,
                emotion=emotion,
                emotion_level=emotion_lvl,
                pitch=pitch,
                speed=speed,
            )

    @parameterized.expand([(5, "haruka", "happiness", 200, 200)])
    async def test_failed_emotion_level(
        self, emotion_lvl, speaker, emotion, pitch, speed
    ):
        with self.assertRaises(MakeException):
            await self.tts.download_voice_byte(
                "test",
                speaker=speaker,
                emotion=emotion,
                emotion_level=emotion_lvl,
                pitch=pitch,
                speed=speed,
            )

    @parameterized.expand([(201, "haruka", "happiness", 1, 200)])
    async def test_failed_pitch(self, pitch, speaker, emotion, emotion_lvl, speed):
        with self.assertRaises(MakeException):
            await self.tts.download_voice_byte(
                "test",
                speaker=speaker,
                emotion=emotion,
                emotion_level=emotion_lvl,
                pitch=pitch,
                speed=speed,
            )

    @parameterized.expand([(401, "haruka", "happiness", 1, 200)])
    async def test_failed_speed(self, speed, speaker, emotion, emotion_lvl, pitch):
        with self.assertRaises(MakeException):
            await self.tts.download_voice_byte(
                "test",
                speaker=speaker,
                emotion=emotion,
                emotion_level=emotion_lvl,
                pitch=pitch,
                speed=speed,
            )
