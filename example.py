import json


class AMIS_EXAMPLE:
    def _extract_examples(self):
        with open("dict-amis.json", newline="", encoding="utf-8-sig") as file:
            data = json.load(file)
        examples = []
        for d in data:
            for obj in d["heteronyms"][0]["definitions"]:
                if "example" in obj:
                    for ex in obj["example"]:
                        examples.append(ex)
        with open("examples.txt", "a", encoding="utf-8-sig") as file:
            for example in examples:
                file.write(example + "\n")
        return "OK"

    def _load_examples(self):
        with open("examples.txt", "r", encoding="utf-8-sig") as file:
            examples = file.readlines()
        return examples

    def find_examples(self, keyword, examples):
        data_list = []
        for ex in examples:
            if keyword in ex:
                amis = ex.split("\ufffa")[0]
                zh_tw = ex.split("\ufffb")[-1]
                print(amis, zh_tw)
                data_list.append({"amis": amis, "zh_tw": zh_tw})
        return data_list


if __name__ == "__main__":
    amis = AMIS_EXAMPLE()

    # 第一次啟動才需執行
    # amis._extract_examples()

    examples = amis._load_examples()
    while True:
        print("請輸入關鍵字：")
        keyword = input()
        data_list = amis.find_examples(keyword, examples)
