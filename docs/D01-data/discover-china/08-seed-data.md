<!-- TARGET-PATH: docs/D01-data/discover-china/08-seed-data.md -->

# 08 · 种子数据

## 1. 类目种子(生产必装 · `system/supabase/seeds/china_categories.sql`)

```sql
insert into zhiyu.china_categories (code, sort_order, name_i18n, description_i18n) values
('01', 1,
 '{"zh":"中国历史","en":"Chinese History","vi":"Lịch sử Trung Quốc","th":"ประวัติศาสตร์จีน","id":"Sejarah Tiongkok"}'::jsonb,
 '{"zh":"朝代更替、历史事件、传奇人物","en":"Dynasties, historical events, legendary figures","vi":"Triều đại, sự kiện lịch sử, nhân vật huyền thoại","th":"ราชวงศ์ เหตุการณ์ ประวัติบุคคล","id":"Dinasti, peristiwa sejarah, tokoh legendaris"}'::jsonb),
('02', 2,
 '{"zh":"中国美食","en":"Chinese Cuisine","vi":"Ẩm thực Trung Quốc","th":"อาหารจีน","id":"Kuliner Tiongkok"}'::jsonb,
 '{"zh":"八大菜系、地方小吃、饮食文化","en":"Eight cuisines, local snacks, food culture","vi":"Tám trường phái, món ăn địa phương, văn hóa ẩm thực","th":"แปดสำรับ อาหารท้องถิ่น วัฒนธรรมอาหาร","id":"Delapan masakan, jajanan daerah, budaya kuliner"}'::jsonb),
('03', 3,
 '{"zh":"名胜风光","en":"Scenic Wonders","vi":"Danh lam thắng cảnh","th":"สถานที่ท่องเที่ยว","id":"Pemandangan Indah"}'::jsonb,
 '{"zh":"自然奇观、历史遗迹、城市地标","en":"Natural wonders, historic sites, city landmarks","vi":"Kỳ quan thiên nhiên, di tích lịch sử, biểu tượng thành phố","th":"ธรรมชาติ โบราณสถาน แลนด์มาร์ก","id":"Keajaiban alam, situs sejarah, ikon kota"}'::jsonb),
('04', 4,
 '{"zh":"传统节日","en":"Festivals & Customs","vi":"Lễ hội truyền thống","th":"เทศกาลและประเพณี","id":"Festival & Adat"}'::jsonb,
 '{"zh":"传统节日、节气、民间习俗","en":"Festivals, solar terms, folk customs","vi":"Lễ hội, tiết khí, phong tục dân gian","th":"เทศกาล สารทฤดู ประเพณี","id":"Festival, musim, adat rakyat"}'::jsonb),
('05', 5,
 '{"zh":"艺术非遗","en":"Arts & Heritage","vi":"Nghệ thuật & Di sản","th":"ศิลปะและมรดก","id":"Seni & Warisan"}'::jsonb,
 '{"zh":"书法、国画、剪纸、陶瓷、刺绣","en":"Calligraphy, painting, paper-cut, ceramics, embroidery","vi":"Thư pháp, quốc họa, cắt giấy, gốm sứ, thêu","th":"การประดิษฐ์ตัวอักษร จิตรกรรม กระดาษตัด เซรามิก ปัก","id":"Kaligrafi, lukisan, kertas potong, keramik, sulam"}'::jsonb),
('06', 6,
 '{"zh":"音乐戏曲","en":"Music & Opera","vi":"Âm nhạc & Hí khúc","th":"ดนตรีและงิ้ว","id":"Musik & Opera"}'::jsonb,
 '{"zh":"民族乐器、京剧、民歌","en":"Folk instruments, Peking Opera, folk songs","vi":"Nhạc cụ dân tộc, kinh kịch, dân ca","th":"เครื่องดนตรีพื้นเมือง งิ้วปักกิ่ง เพลงพื้นบ้าน","id":"Alat musik etnis, opera Beijing, lagu rakyat"}'::jsonb),
('07', 7,
 '{"zh":"文学经典","en":"Classic Literature","vi":"Văn học kinh điển","th":"วรรณกรรมคลาสสิก","id":"Sastra Klasik"}'::jsonb,
 '{"zh":"古典名著、诗词歌赋、寓言","en":"Classic works, poetry, fables","vi":"Tác phẩm kinh điển, thi ca, ngụ ngôn","th":"วรรณกรรม กวีนิพนธ์ นิทาน","id":"Karya klasik, puisi, fabel"}'::jsonb),
('08', 8,
 '{"zh":"成语典故","en":"Idioms & Allusions","vi":"Thành ngữ & Điển cố","th":"สำนวนและตำนาน","id":"Idiom & Kisah"}'::jsonb,
 '{"zh":"成语故事、歇后语、谚语","en":"Idiom stories, two-part allegorical sayings, proverbs","vi":"Câu chuyện thành ngữ, yết hậu ngữ, tục ngữ","th":"นิทานสำนวน คำพังเพย สุภาษิต","id":"Kisah idiom, peribahasa dua bagian, pepatah"}'::jsonb),
('09', 9,
 '{"zh":"哲学思想","en":"Philosophy & Wisdom","vi":"Triết học & Trí tuệ","th":"ปรัชญาและภูมิปัญญา","id":"Filsafat & Kebijaksanaan"}'::jsonb,
 '{"zh":"儒释道、诸子百家","en":"Confucianism, Buddhism, Daoism, Hundred Schools","vi":"Nho-Phật-Đạo, bách gia chư tử","th":"ขงจื๊อ พุทธ เต๋า นักปราชญ์ร้อยสำนัก","id":"Konfusianisme, Buddhisme, Taoisme, Seratus Aliran"}'::jsonb),
('10', 10,
 '{"zh":"当代中国","en":"Modern China","vi":"Trung Quốc hiện đại","th":"จีนสมัยใหม่","id":"Tiongkok Modern"}'::jsonb,
 '{"zh":"科技、城市生活、流行文化","en":"Technology, urban life, pop culture","vi":"Công nghệ, đời sống đô thị, văn hóa đại chúng","th":"เทคโนโลยี ชีวิตเมือง วัฒนธรรมป๊อป","id":"Teknologi, kehidupan kota, budaya pop"}'::jsonb),
('11', 11,
 '{"zh":"趣味汉字","en":"Fun with Chinese","vi":"Hán tự thú vị","th":"อักษรจีนสนุก","id":"Aksara Tiongkok Seru"}'::jsonb,
 '{"zh":"汉字演变、数字密码、网络用语","en":"Character evolution, number codes, internet slang","vi":"Diễn biến chữ Hán, mật mã số, tiếng lóng mạng","th":"วิวัฒนาการอักษร รหัสตัวเลข ศัพท์เน็ต","id":"Evolusi aksara, kode angka, slang internet"}'::jsonb),
('12', 12,
 '{"zh":"神话传说","en":"Myths & Legends","vi":"Thần thoại & Truyền thuyết","th":"เทพปกรณัมและตำนาน","id":"Mitos & Legenda"}'::jsonb,
 '{"zh":"创世神话、神仙体系、民间传说","en":"Creation myths, pantheon, folk legends","vi":"Thần thoại sáng thế, hệ thống thần tiên, truyền thuyết dân gian","th":"ปกรณัมการสร้างโลก เทพเจ้า ตำนานพื้นบ้าน","id":"Mitos penciptaan, panteon, legenda rakyat"}'::jsonb)

on conflict (code) do update set
  sort_order       = excluded.sort_order,
  name_i18n        = excluded.name_i18n,
  description_i18n = excluded.description_i18n,
  updated_at       = now();
```

> 上述外语翻译为初稿,后续由翻译团队审校。

## 2. dev 示例:2 篇文章 + 5 句

> 仅本地与 dev 环境 seed,**不入生产**;位置 `system/supabase/seeds/dev/china_articles_dev.sql`。

完整示例(秦始皇统一六国 / 宫保鸡丁)请见信息源 [`function/01-china/ai/F1-AI-数据模型规范/09-种子数据.md §2`](../../../function/01-china/ai/F1-AI-数据模型规范/09-种子数据.md),反向回写期保留原文不再重复;落地任务详 D02。
