class Evaluator:

    def zip_evaluate(coefs, words):
        if (len(coefs) != len(words)):
            print("-1")
            return -1
        res = 0
        for mul, s in zip(coefs, words):
            res += len(s) * mul
        print(res)
        return res

    def enumerate_evaluate(coef, words):
        if (len(coefs) != len(words)):
            print("-1")
            return -1
        res = 0
        for index, value in enumerate(coefs):
            for ind, val in enumerate(words):
                if index == ind:
                    res += len(val) * value
        print(res)
        return res

words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
Evaluator.zip_evaluate(coefs, words)
Evaluator.enumerate_evaluate(coefs, words)

print("---")

words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
Evaluator.zip_evaluate(coefs, words)
Evaluator.enumerate_evaluate(coefs, words)

