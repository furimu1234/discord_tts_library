from __future__ import annotations

import os
from unittest import IsolatedAsyncioTestCase

from parameterized import parameterized

from tts import API_KEY, BASE_URL, Tts

# TODO: 出来ればアクセスしたくないけどエラーモックめんどくさい


class TestMakeFile(IsolatedAsyncioTestCase):
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
    async def test_success_make_file(self, speaker, emotion, emotion_lvl, pitch, speed):
        bynary = await self.tts.download_voice_byte(
            "test",
            speaker=speaker,
            emotion=emotion,
            emotion_level=emotion_lvl,
            pitch=pitch,
            speed=speed,
        )
        self.assertIsNotNone(bynary)

        if not bynary:
            return

        channel_id = 12345
        message_id = 234567

        await self.tts.save_wave_file(
            bynary, channel_id=channel_id, message_id=message_id
        )

        fp = f"voices/{channel_id}/{message_id}.wav"

        self.assertEqual(os.path.exists(fp), True)
        os.remove(fp)
