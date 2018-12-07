import speech_recognition as sr
from termcolor import colored


class RecordIntepreter():

    key_word = ["重點", "考試"]

    def add_keyword(self, word):
        self.key_word.append(word)

    def print_result(self, file_path):
        test_record = sr.AudioFile(file_path)
        r = sr.Recognizer()
        with test_record as source:
            audio = r.record(source)
            audio_content = r.recognize_google(audio, language="zh-TW")

        if audio_content:
            for i in range(len(self.key_word)):
                if self.key_word[i] in audio_content:
                    audio_content = audio_content.replace(self.key_word[i], colored(self.key_word[i], "green",))

        print(audio_content)


if __name__ == "__main__":
    record_intepreter = RecordIntepreter()
    record_intepreter.add_keyword("雞排")
    record_intepreter.print_result("./record/1207-2.wav")

