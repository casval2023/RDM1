import streamlit as st

# 問題と解答のデータ
data = {
    "問1": {
        "question": "新陳代謝についての正しい意味を下記より選んでください。",
        "options": ["①汗をかくこと", "②食べ物を消化すること", "③細胞が生まれ変わること"],
        "answers": ["③細胞が生まれ変わること"]
    },
    "問2":{
        "question": "A～Cの言葉を下記の語群から選び、文章を完成させましょう。皮膚や髪の毛、背骨を含む骨などの体のすべての部位、器官は次々と新しい細胞に生まれ変わっていきます。少なくとも（　A　）か月間で、（　B　）兆個とも言われる人間の体のすべての細胞が生まれ変わるということになります。人体で一番早く細胞が生まれ変わるところは（　C　）の中と言われます。",
        "options": ["①１", "②２", "③３", "④50", "⑤60", "⑥100", "⑦お腹", "⑧口"],
        "answers": ["③３", "⑤60", "⑧口"]
    },
    "問3": {
        "question": "A～Cの言葉を下記の語群から選び、文章を完成させましょう。新陳代謝をしている間に、摂取エネルギーが（　A　）量を大幅に（　B　）回るようなダイエットは非常に危険です。食べないで痩せるダイエットは脂肪を減らすだけでなく、（　C　）や骨まで削ってしまい、さらにはやる気や前向きな気持ちまでもを衰退させてしまうという事になりかねません。",
        "options": ["①基礎代謝", "②消費エネルギー", "③水分", "④下", "⑤上", "⑥生命", "⑦筋肉"],
        "answers": ["①基礎代謝", "④下", "⑦筋肉"]
    },
    "問4": {
        "question": "BMI（ボディ・マス・インデックス）「体格指数」は世界で最も広く使われている肥満判定用の物差しです。正しい計算方法を下記より選んでください。",
        "options": ["①体重（kg)　÷　身長（cm)　÷　身長（cm)", "②体重（kg)　÷　胴回り（cm)　÷　身長（m）", "③体重（kg)　÷　身長（m）　÷　身長（m)"],
        "answers": ["③体重（kg)　÷　身長（m）　÷　身長（m)"]
    },
    "問5": {
        "question": "A～Cの言葉を下記の語群から選び、文章を完成させましょう。日本肥満学会では一番病気になりづらいBMI値を（　A　）としていますが、女性のBMI（　B　）は骨格や筋肉量など男性との違いにより、日本ダイエットアカデミー協会では女性の健康体重をBMI（　C　）とし、男性ではBMI（　B　）を健康体重とし、推奨しています。",
        "options": ["①30", "②25", "③20", "④22", "⑤18", "⑥19～20", "⑦18～21", "⑧20～22"],
        "answers": ["④22", "④22", "⑥19～20"]
    },
    "問6": {
        "question": "A～Cの言葉を下記の語群から選び、文章を完成させましょう。私たちの体は、水分をほとんど含まない（　A　）と、筋肉や骨、体液など水分を多量に含む（　B　）の二つに大別され、（　A　）は水分が少ない分、電気が通りにくく電気抵抗が上昇します。この原理を応用して、手足の電極から微量な電流を流し、体重と同時に体全体の（　C　）（電気抵抗）を測定し簡単に体脂肪率を推定することができます。人体の（　C　）は刻々と変化しており、朝の起床時が一番高く、夕方から夜にかけて安定していきます。",
        "options": ["①脂肪組織", "②細胞組織", "③除脂肪組織", "④インピーダンス", "⑤コレステロール"],
        "answers": ["①脂肪組織", "③除脂肪組織", "④インピーダンス"]
    },
    "問7": {
        "question": "A～Cの言葉を下記の語群から選び、文章を完成させましょう。肥満は「（　A　）のわりに体重が重すぎる状態」ではありません。水を飲んでも、野菜を大量に食べても体重は増加しますが、それは「肥満」とはいいません。脂肪が増えた場合を（　B　）といい、一時的に水分が増えた場合を（　C　）といいます。",
        "options": ["①身長", "②年齢", "③脂肪過多", "④肥満", "⑤浮腫（むくみ）", "⑥貧弱"],
        "answers": ["①身長", "④肥満", "⑤浮腫（むくみ）"]
    },
    "問8": {
        "question": "A～Cの言葉を下記の語群から選び、文章を完成させましょう。BMIから「太りすぎ」と判定された方の2～3割は筋肉や骨が多くて体重が重い（　A　）という人たちで肥満ではありません。一方、BMIから「正常体重」や「低体重」と判定された人の中にも、体脂肪率の高いいわゆる（　B　）と呼ばれる方がいます。ですから、からだに占める脂肪組織の割合（体脂肪率）や（　C　）量を測定できると、BMIだけではわからない一歩踏み込んだ正確な判定が可能になります。",
        "options": ["①筋肉質", "②かた太り", "③肥満", "④かくれ肥満", "⑤水分", "⑥基礎代謝"],
        "answers": ["②かた太り", "④かくれ肥満", "⑥基礎代謝"]
    },
    "問9": {
        "question": "Aにあてはまる言葉を下記①～③から１つ選び、文章を完成させましょう。１kgの体脂肪を燃焼させるには、消費エネルギーと摂取エネルギーの差が、合計（　A　）kcalマイナスになればよいということですが、これを運動量だけで消費することはとても大変です。例えば、代表的な有酸素運動であるフルマラソンを2時間半で走破しても、2400kcal前後のエネルギーしか消費されないのです。",
        "options": ["①5200", "②6200", "③7200"],
        "answers": ["③7200"]
    }
}

def main():
    st.title('レギュラーダイエットマスター第1章復習問題')
    score = 0
    for key, value in data.items():
        st.write(f"### {key}")
        st.write(value["question"])
        answers = st.multiselect("選択肢を選んでください:", value["options"])
        if answers == value["answers"]:
            score += 1
            st.write("正解です！")
        #else:
            #st.write("不正解です。")
            #st.write(f"正解は {value['answers']} です。")
    st.write(f"### スコア: {score}/{len(data)}")
    st.write(f"# 正答率は **{round(score * 100/ len(data))}%** です！")

if __name__ == "__main__":
    main()
