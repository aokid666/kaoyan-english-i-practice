"""Build the public, answer-free catalogue from complete and reconstructed sets."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
entries = [
    {
        "id": "2026-10-02-01", "date": "2026-10-02", "number": 1,
        "title": "同伴学习 · 周末活动 · 校园物品交换", "kind": "双图表",
        "translation": {
            "topic": "同伴学习与讲座",
            "text": """Directions: Read the following text carefully and translate the marked part into Chinese.

A classroom lecture can introduce a set of ideas, but students may discover what they have not understood only when someone asks them to explain those ideas. A study published in September 2026 examined this possibility among 88 undergraduates at a medical school in Saudi Arabia. The students were assigned to four groups: a lecture alone, peer learning alone, a lecture followed by peer learning, or the same two activities in reverse order.

All four groups took a test before and after the lesson. Their initial scores were similar. On the later test, both groups that combined the two activities scored considerably higher than the groups that used either activity alone. The order of the lecture and peer learning made little difference to that broad result. 【待译部分】The comparison suggests that hearing an explanation and then discussing it may help students connect concepts, though results from a single medical school cannot establish how the same approach would work in every classroom.【待译部分结束】

The researchers also found that the peer-learning-only group scored higher than the lecture-only group. These findings concern performance on the test used in this study; they invite further questions about the conditions under which students benefit most from explaining ideas to one another.

要求：仅翻译标出的部分。""",
            "source": "Humanities and Social Sciences Communications · 2026-09-25 · More minds, more learning: integrating peer learning with lectures to boost conceptual understanding in medical education",
            "url": "https://www.nature.com/articles/s41599-026-09271-9"
        },
        "partA": {
            "topic": "完整来信回复：两项周末活动",
            "text": """Directions:

Suppose your friend Alex, who will visit your city, has sent you the following email. Write him a reply.

Dear Li Ming,

Your university is holding two events on Saturday, October 17. There is a guided walk along the riverside from 2:00 to 3:30 p.m., and a printmaking workshop from 2:00 to 4:00 p.m. I can attend only one. I enjoy being outdoors, but I also like making things, so I cannot decide. The walk is free; the workshop costs a small fee, which I can afford. Which would you recommend, and why? If you're available, would you come with me? Please let me know by Monday, since registration closes then.

Best,
Alex

Write your email in about 100 words on the ANSWER SHEET. Do not use your own name. Use “Li Ming” instead. Do not write the address. (10 points)"""
        },
        "partB": {
            "directions": """Directions:

Write an essay of 160–200 words based on the two charts below. In your essay, you should:
1. describe the charts briefly,
2. explain the situation reflected in them, and
3. give your comments.

Write your answer on the ANSWER SHEET. (20 points)""",
            "image": "./assets/2026-10-02-charts.png"
        }
    },
    {
        "id": "2026-09-20-02", "date": "2026-09-20", "number": 2,
        "title": "四天工作制 · 印刷服务 · 双幅图画", "kind": "双幅图画",
        "translation": {
            "topic": "四天工作制长期调整",
            "text": """Directions: Read the following text carefully and translate the marked part into Chinese.

Reducing the working week raises a question that a short trial cannot fully answer: how does the arrangement survive after the initial enthusiasm has faded? A recent study followed a software organization operating a four-day, thirty-two-hour week. Drawing on fifteen interviews conducted in 2022 and 2026, the researchers examined how working practices developed over time.

Employees adjusted meetings, communication and the organization of tasks to fit the shorter schedule. Later, the company faced changes in ownership and economic conditions. 【待译部分】The arrangement was sustained not by leaving the original rules untouched, but by revising everyday practices through which employees coordinated their work, a process that became more demanding as conditions outside the organization changed.【待译部分结束】

The researchers therefore describe the shorter week as an evolving arrangement rather than a single reform completed at the moment of introduction. Their account concerns one organization, so it cannot establish that the same approach would succeed everywhere. It does, however, suggest a useful question for further investigation: whether the capacity to adjust working practices matters as much as the decision to reduce hours.

要求：仅翻译标出的部分。""",
            "source": "arXiv · 2026-09-11 · Beyond Establishing the Four-Day Workweek: Understanding Adaptation and Long-Term Survival in an Agile Software Organization",
            "url": "https://arxiv.org/abs/2609.13089"
        },
        "partA": {
            "topic": "主动邮件：印刷材料问题",
            "text": """Directions:

Suppose you are Li Ming. You ordered a printed course reader from your university’s printing service. When you collected it yesterday, you found that several pages were missing and others were printed twice. You need the complete reader for a seminar in two days.

Write an email to the manager of the printing service to explain the problem and request an appropriate solution. You may include relevant details.

Write your email in about 100 words on the ANSWER SHEET. Do not use your own name. Use “Li Ming” instead. Do not write the address. (10 points)"""
        },
        "partB": {
            "directions": """Directions:

Write an essay of 160–200 words based on the two pictures below. In your essay, you should:
1. describe the pictures briefly,
2. interpret their meaning, and
3. give your comments.

Write your answer on the ANSWER SHEET. (20 points)""",
            "image": "./assets/2026-09-20-pictures.png"
        }
    },
    {
        "id": "2026-09-20-01", "date": "2026-09-20", "number": 1,
        "title": "花园雕塑 · 演讲比赛 · 社区食堂", "kind": "数据表",
        "translation": {
            "topic": "旧雕塑的重新发现",
            "text": """Directions: Read the following text carefully and translate the marked part into Chinese.

For more than seventy years, a marble bust stood in an English garden without being recognized as a significant work of art. Covered in lichen, it was treated as an ordinary decoration. A report in Smithsonian Magazine describes its identification as a sculpture of Daphne, a figure from Greek mythology, made by the American artist Harriet Goodhue Hosmer.

【待译部分】Only when the object was examined during a routine property valuation did its connection with a nineteenth-century sculptor emerge, revealing how easily an artwork can remain familiar to its owners yet absent from their understanding.【待译部分结束】

Hosmer's name appears on the back of the sculpture. She worked in Rome at a time when professional opportunities for women were severely restricted. Such information places the object within a history that its location alone could not communicate. The episode invites a distinction between preserving an object physically and recognizing its significance. Something may survive for generations while the knowledge needed to interpret it is lost, overlooked or never acquired by those who live with it.

要求：仅翻译标出的部分。""",
            "source": "Smithsonian Magazine · 2026-09-17 · A Rare Marble Sculpture by America’s First Professional Female Sculptor Sat Hidden in Plain Sight for Decades in an English Garden",
            "url": "https://www.smithsonianmag.com/smart-news/a-rare-marble-sculpture-by-americas-first-professional-female-sculptor-sat-hidden-in-plain-sight-for-decades-in-english-garden-180989508/"
        },
        "partA": {
            "topic": "回复：感谢祝贺并说明备赛",
            "text": """Directions:

Suppose you are Li Ming. Your friend Alex has written to congratulate you on winning your university's English speech contest. He plans to enter a similar contest next month and would like to know how you prepared, especially how you managed to speak without reading from a script.

Write him an email to thank him and respond to his request. You may include relevant details.

Write your email in about 100 words on the ANSWER SHEET. Do not use your own name. Use “Li Ming” instead. Do not write the address. (10 points)"""
        },
        "partB": {
            "directions": """Directions:

Write an essay of 160–200 words based on the table below. In your essay, you should:
1. describe the table briefly,
2. explain the situation reflected in it, and
3. give your comments.

Write your answer on the ANSWER SHEET. (20 points)""",
            "table": """某市不同年龄居民选择社区食堂的首要原因（2026年）
首要原因　　　　　　　18—35岁　36—59岁　60岁及以上
节省做饭时间　　　　　　46%　　　32%　　　15%
价格实惠　　　　　　　　28%　　　30%　　　25%
饮食营养均衡　　　　　　16%　　　26%　　　32%
方便与他人一起用餐　　　10%　　　12%　　　28%
注：训练数据；每组200名过去一个月使用过社区食堂的居民；单选。"""
        }
    },
]

historic = json.loads((ROOT / "historic_reconstructions.json").read_text(encoding="utf-8"))
entries.extend(historic)

(ROOT / "entries.json").write_text(json.dumps(entries, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
