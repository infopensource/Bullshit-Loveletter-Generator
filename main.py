
import time
import random

name=input("请输入女友姓名: ")
lines=int(input("需要生成几段: "))-2

adj1=['天生丽质','慧质兰心','秀外慧中','暗香盈袖','倾国倾城','温婉娴淑','千娇百媚','仪态万千','美艳绝世','国色天香','花容月貌','明目皓齿','淡扫峨眉','清艳脱俗','香肌玉肤','清丽绝俗','仪态万端','婉风流转','美撼凡尘','聘婷秀雅','娥娜翩跹','俏丽多姿','如花似月']
adj2 =['闭月羞花','沉鱼落雁','倾国倾城','千娇百媚','明目皓齿','淡扫峨眉','清艳脱俗','香肌玉肤','婉风流转','美撼凡尘','聘婷秀雅','娥娜翩跹','俏丽多姿','风姿卓越','顾盼流转','清丝纠缠','举步轻摇','剪水双瞳','美艳绝伦','神仙玉骨','如花似玉','一代佳人','一代容华','红粉佳人','红粉青娥','天生尤物','天仙化人','姑射神人','绝色美人','月里嫦娥','天生丽质','天香国色','仙资玉质','妍资艳质','夭桃秾李','色艳桃李','华如桃李','桃羞杏让','如花似月','羞花闭月','花容月貌','芙蓉如面','粉白黛黑','娇艳惊人','冠觉群芳','桃腮杏脸','樱桃小口','婀娜多姿','丰姿绰约','娉婷袅娜','国色天姿','倾国倾城','国色天香','婀娜多姿','亭亭玉立','粉面桃花','肤如凝脂','声若莺啼','明眸皓齿','花容月貌','风华绝代','楚楚动人','冰清玉洁','杨柳细腰','气质清纯','容颜秀美','婉约可人','天生丽质','美丽大方','清秀大方','体态轻盈','气质高雅','温柔体贴','知书达礼','仪态万千','艳冠群芳','楚楚动人','秀外慧中','风情万种','知书达理','温文尔雅','空谷幽兰','超凡脱俗','兰心蕙质','秀外慧中']
adj3= ['善良','温柔','善解人意','小鸟依人','聪明','可爱','文静','活泼','冰雪聪明','美丽','可人','羞涩','艳丽','妍丽','美艳','富丽','瑰丽','秀丽','鲜艳','绚丽','漂亮','摩登','大方','时兴','入时','姣好','俊美','俊丽','俊秀','俊俏','斑斓','大度','文雅''明媚皓齿']

text=['春水初生,春林初盛,春风十里,不如睡你。',
 '外面风大，跟我回家。',
 '留在我身边，远近我都接受。',
 '向来没耐心的我，在你身边徘徊了这么久。',
 '你站的方向风吹过来都是暖的。',
 '你陪着我的时候，我从来没有羡慕过任何人。',
 '因为有你我才能笑着摇头拒绝所有诱惑和暧昧。',
 '我喜欢你只有一个理由，你就是理由。',
 '你快乐所以我快乐，快乐都是你给的。',
 '如果你最后一贫如洗，我将是你最后的行李。',
 '遇见你是所有故事的开始。',
 '陪我走走吧，趁天还没亮浓雾里还透着光。',
 '我也憧憬过，也怕后来没结果。',
 '所有的不愉快都改变不了我对你的坚持。',
 '你在身边，世界只剩一个焦点。',
 '陪你走到底只要你愿意。',
 '我没有信仰。对于我，你比信仰重要。',
 '如果你能真诚的为我张开快乐，我愿意抛弃一切为你执着。',
 '你可知道你的名字解释了我的一生。',
 '我这一途所遇风景太多，却也不抵你一眼。只盼化身一尾黑纹金鱼，栖于你眉目。不惧终成一个溪水枯竭的结局，只怕你无人相伴。',
 '我没有很刻意的去想念你，因为我知道，遇到了就应该感恩，路过了就需要释怀。我只是在很多很多的小瞬间想起你，比如一部电影，一首歌，一句歌词，一条马路和无数个闭上眼睛的瞬间。',
 '原来你是我最想留住的幸运。',
 '如果我说不吻你不罢休，谁能逼我将就。',
 '一次就好，我带你去看天荒地老。',
 '我为你翻山越岭，却无心看风景。',
 '就算今天我把话说的再绝，明天醒来还是会喜欢你，我多没出息这你知道。',
 '如果全世界都对你恶语相加，我就对你说上一世情话。',
 '除了你，万敌不倾。',
 '没关系你也不用给我机会，反正我还有一生来浪费。',
 '回头我就在。',
 '你是雾你是旧梦，你是写在烟盒上的诗，你是我心上的一间小酒馆。',
 '为你，千千万万遍，就让我等一等再放弃。',
 '不希望你被太多人喜欢，我喜欢就好。',
 '哪有什么突然想起你，其实一直在心里。',
 '只要见到你，无论多糟，我都会笑。',
 '我想用余生为你暖一盏茶，晚风微扬时勿忘归家。',
 '你是烈酒，入喉汹涌，一口咽不下，余生慢慢尝。',
 '若有朝一日无处可去，不妨归来，把我当做岁月的尽头。'
 '待在我身边，我怕你危险。',
 '只尊你为王，为你披荆斩棘战四方。',
 '我命由你不由天。',
 '我从不说情话，我对你的每一句话每一个字，都是肺腑之言。',
 '与你相携途中，一切皆为风景。',
 '你的名字是多美的情诗。',
 '遇一人白头，择一城终老。',
 '星辰点缀在你肩上，你眼中有整片海洋。',
 '最好的幸福是你给的在乎。',
 '一辈子只面对一个人，想想就可怕。但是如果是眼前这个人的话，我想我可以赌一下。',
 '若能与君相共度，又何惧荆棘载途。',
 '曾引相思种，春来希盛开，穷冬驱不去，卿在万里外。',
 '愿陪你从天光乍破，走到暮雪白头。',
 '你若撒野，今生我把酒奉陪。',
 '哪怕你受尽千夫所指，我亦护定你。',
 '你走，我不送你。你来，无论多大风多大雨，我要去接你。',
 '你的过去我来不及参与，你的未来我奉陪到底。',
 '何其有幸，此生遇到你。',
 '生命那么短，世界那么乱，我不想争吵，不想冷战，不愿和你有一秒遗憾。',
 '余生请你多指教。',
 '我不怕天黑和惊雷，只怕你心酸和皱眉。',
 '不是因为我执着，而是因为你值得。',
 '每一次我想你，全世界每一处都是你。',
 '你没那么好，只是谁都替代不了。',
 '你拿枪指着我的胸口，就算枪响我也相信只是走火。',
 '时光温热，岁月静好。你还没来，我怎敢老。',
 '只要你的目光还注视着我，我的眼里就永远走不进别人。',
 '如过没有你，明天不值得期待，昨天不值得回忆。',
 '你是我不喜欢别人的理由。',
 '千山万水任时光后退，也只希望在你身边徘徊。',
 '你可知我百年的孤寂只为你一人守候，千年的恋歌只为你一人而唱。',
 '我一生中最美好的时光是，当我和你成为“我们”。',
 '以诗为梦马，以你为年华。',
 '介意你的好多缺点却又统统妥协接受。',
 '不是除了你我就没人要，只是除了你我谁都不想要。',
 '只要你一直在我身边，其他东西不再重要。',
 '傻笑不是与生俱来的，而是由我爱上你的那一刻开始的。',
 '我希望这个世界可以很小很小，小到我一转身就可以看见你。',
 '我不想做你生命的插曲，只想做你生命最完美的结局。',
 '纵然有百万个理由离开你，我也会寻找一个理由为你留下。',
 '希望吹过我的风还能绕几圈去拥抱你。',
 '听说晚安是最情长的告白，但我只知道早安是最深情的问候。',
 '我哪有什么好脾气，我的好脾气，还不是因为爱你。',
 '一辈子有多少来不及我不管，庆幸的是我来得及爱你。',
 '如果我的未来有你在，那其他的什么我都不怕了。',
 '情话很多，我只想与你细水长流。',
 '你若不离，我亦不弃。',
 '万千灯火，就是看上了你。',
 '我喜欢春天的花夏天的树秋天的黄昏冬天的太阳和每天的你。',
 '我给不了你太多，但有个词叫尽我所能。',
 '你在人潮里不知所措，我却跟在你身后，伸手怕犯错，缩手怕错过。',
 '我感觉我是世界上眼光最好的人，因为我看上了你。',
 '总觉得用一个脑袋想你是不够的。',
 '为什么这么多人中偏偏是你，也许是那天阳光正好，微风不燥，你也刚好在笑。',
 '现在想想，我爱你就像，天刮风，云下雨，没有理由没有征兆的就来了。',
 '我是个很慢热的人，但我保温性能很好，一旦热起来，就不会凉下去，比如我喜欢你。',
 '人潮好拥挤，我却只想爱你。',
 '你不需要多好，我喜欢就好。',
 '你一百种样子，我一百种喜欢。',
 '我希望十年后有一场婚礼的主角是你和我，我对着你说我愿意。',
 '若有幸来世再见，长路携手，岁月悠悠，你说从头就从头。',
 '你的名字就几笔，却贯穿了我整个年华。',
 '我不想和别人拥抱，因为那里没有你的心跳。',
 '第一眼就心动的人要怎么做朋友。',
 '我心里数落了你千万条缺点，却抵不过看到你的那一眼。',
 '我向来口笨唇拙，除了爱你什么都不会说。',
 '我必须要看过最蓝的天，爬过最高的山，路过最大的草原，听过最澎湃的海潮声，才有资格说在这个世界上，我最想呆在你身边。',
 '纵然万劫不复，纵然相思入骨，我也待你眉眼如初，岁月如故。',
 '我不想要输赢自尊虚荣了，我想要你。',
 '熬过山头不知风霜的春秋，正午时分我来叩门，走吧，我们去流浪。',
 '等你走到有些累了的时候，我还会借你我的左肩。',
 '在有生的瞬间能遇到你，竟花光我所有运气。',
 '愿山野都有雾灯，你手持火把渡岸而来点亮我孤妄的青春，此后夜车不再驶往孤站，风雨漂泊都能归舟。',
 '一百年很久，有的是时间，每一笔我都不想错过，每一分都不舍抵赖。',
 '慢下来，不要太快，不要怕晚，我们一起拨乱算珠，这一笔互相打个欠条，带进坟墓里，带进来生的记忆里，下辈子，再继续算。',
 '我曾以为我孤独长命，却仍能有幸与你同行在漫长缺氧的枯朽之年的罅隙里。',
 '我爱你胜过爱我自己。',
 '你若觉得高处不胜寒，我便拱手江山讨你欢。',
 '我拒绝更好更圆的月亮，拒绝未知的疯狂，拒绝声色的张扬，不拒绝你。',
 '你是薄雾，是暖风，我喜你依旧浓。',
 '与君初相识，犹如旧人归。',
 '你说人山人海边走边爱怕什么孤单，我说人潮汹涌都不是你该怎么将就。',
 '如果我不曾见过你，我本可以忍受黑暗。如果我不曾遇到你，我本可以一个人也过得很好。',
 '你就像一个信仰，再痛也会向往。',
 '我有孤独和酒，你跟不跟我走？',
 '每天都忍不住去想你，这算不算习惯。',
 '玫瑰是偷的，但爱你是真的。',
 '不想说醉人的情话，我只想带你回家。',
 '如果有你在前方，路再坎坷都是旅行。',
 '即使身边世事再毫无道理，与你永远亦连在一起。',
 '你是我三十九度的风，风一样的梦。',
 '我希望你可以是我的独家记忆。',
 '愿岁月可回首，且以深情共白头。',
 '人来人往我在你身后，张望多久都无妨。',
 '如果所有土地连在一起，走上一生只为拥抱你。',
 '余生太长，你好难忘。',
 '爱经不起遗憾的事，身边的人不可以不是你。',
 '你口中的风景我都觉得好美丽，不过是因为我喜欢你。',
 '我想听你所有的故事，好的坏的，一切。',
 '手的另一边伸给你牵，向南向北我都情愿。',
 '不为日子皱眉头，答应你，只为吻你才低头。',
 '要我等你多久，十个春天够不够？',
 '想听你说情话，抱着你看雪花。',
 '我以为除了你，我喝什么都喝不醉。可好像世间万物又都掺着你，我呼吸会醉，沉默也醉。',
 '若是你看倦了风景，走累了路，我愿意变成酒色的石头，让你把余生靠一靠。',
 '愿你洗去白天的浮躁不安，愿你在每个夜里都能安然入睡美梦相伴。',
 '很多东西看久了都会腻，唯独你，越看越欢喜。',
 '我一生荒芜，唯记得同你在一起时笑的盎然肆意，哭的酣畅淋漓。',
 '你是海，是归船，是遍山翠藤，是诗人的眼泪，是黄昏树梢上挂着的那朵夕阳，是这世间所有美好事物的代表。',
 '灼灼桃花十里，只取你一朵放在心上足矣。',
 '你知道什么叫意外吗，就是我从没想过会遇见你，但我遇见了；我从没想过会爱你，但我爱了。',
 '我在想你收到我的短信，你会不会粲然一笑，就像我收到你的信息一样开心。',
 '每段青春都会苍老，但我希望记忆里的你一直都好。',
 '有些歌听前奏就爱上了，有些作业打开第一页就不想做了，有些人看第一眼就爱上了，比如你。',
 '喜欢天空的颜色大海的深度和你的声音。',
 '你是我穷极一生做不完的一场梦。',
 '深林时见鹿，海蓝时见鲸，梦醒时见你。',
 '你的名字，你的眼睛，你的笑，你的好。我没忘，没敢忘，也没想忘。',
 '你给我半点微笑，我都当个宝，想要炫耀。',
 '我不想和你放荡不焉浪完青春，只想和你安安稳稳到枕边人。',
 '你总有一天会知道，来往的人中，我是最爱你的。',
 '你发的“嗯”都比别人的好看。',
 '除了你再也没有人能住进我的眼睛。',
 '想带着你走过春秋，穿过清晨雨露，傍晚云霞，历经沧桑人世，而我依旧爱你如初。',
 '你在我后半生的城市里。',
 '我爱你，不只是说说而已。',
 '纵使喝醉酒满嘴胡话，也有一句好想你是发自肺腑。',
 '你是我期待又矛盾的梦想，抓住却不能拥抱的风，想喝又怕醉的酒。',
 '我放你去浪，等你尝过所有新鲜感，等你终于感到了厌倦，我还等你呢。',
 '我没有讨好你的天分，但我比谁都认真。',
 '我身边并不拥挤，你来了就是唯一。',
 '你是我的梦，像北方的风。',
 '我曾经风沙尘土一马一夕，忘记所有人却唯独爱上你。',
 '你一笑我高兴很多天，你一句话我记好多年。',
 '我行过许多地方的桥，看过许多次数的云，喝过许多种类的酒，却只爱过一个正当最好年龄的人。',
 '你是我光是想想都会偷着乐的人。',
 '我最喜欢的一个字是吃，两个字是旅行，三个字是你名字。',
 '你三三两两的醉语，我将嗔痴一饮而尽。',
 '你一直住在我的心里久到变成了房东。',
 '我从远方赶来，恰好你也在。',
 '我不喜欢这个世界，但我喜欢你。',
 '喜你是疾，药石无医。',
 'Will you be my lover？',
 ' Will you be the one？',
 '最好闻的是，抱你时你身上的味道。',
 '好像你说什么都是好听的，可以淡化悲伤，也能燃起热潮。',
 '不敢凝视你的眼睛，是怕我每个眼神都在表白。',
 '春天会下雪，夏天有大雨，秋天会起风，冬天有艳阳。一年四季会有很多意外，但最迷人的，还是遇见了你。',
 '只要你在身边，去哪里都是风景。',
 '你所有为人称道的美丽，都不及我第一次遇见你。',
 '我见过千万人，像你的发，像你的眼，但都不是你的脸。',
 '因为爱你，所以看谁都像情敌。',
 '我不知道我为什么爱你，就像我无法描述水是什么味道一样。但我知道我需要你，就像我需要水一样。',
 '我本来打算告诉你，当你不在我身边时，我所遇到的所有糟糕事。但最后，我只想告诉你，我很想你。',
 '世界上最短的咒语，是你的名字。',
 '喜欢你，就是心里放弃了一千次也会在你说一句好听的话再奋不顾身一万次。',
 '很多时候我对一个人的喜欢就像是兜里揣了一块糖，想跟别人显摆，又不想给别人吃。',
 '你应该被抱紧，有风我来顶。',
 '我愿拿青春换酒共你白头。',
 '最在乎的人，最重视的人，最特别的人，最珍惜的人，都是同一个你。',
 '无论我变得如何强大，你仍然是我的弱点。',
 '每一次我想你，全世界每一处都是你。',
 '自从认识了你，我就没打算忘了你。',
 '我以为我百毒不侵，却唯独对你上了瘾。',
 '世间的五味俱全，谢谢你给我的甜。',
 '不羁岁月磨白头，一个你一壶酒，便是盼头。',
 '陪你走的青春是我一生一次的认真。',
 '你知我从未惧怕奔赴，不过是因为你在路的尽头。',
 '修你一世平安喜乐，护你百岁无忧安康。',
 '没有你，良辰美景更与何人说。',
 '我们路过多少风景，看过多少路标，多少故事藏在心里，多少言语无人倾听。咖啡换了第几杯，身旁经过多少人，心里藏着的那些歌，想唱给的人都是你。',
 '我想不出来第一次看见你的时候，你穿的衣服是什么颜色。是晴天还是雨天，因为我从未想到那天之后我会喜欢你。',
 '天空很蓝，风很凉爽，景很动人，好看的人更多，但所有的这些，都不及你。',
 '我不怕老，也不怕死，只怕我所深爱的你过得不好。',
 '车马很慢，阳光很懒，你很好看。',
 '就算大雨让整座城市颠倒，我会给你怀抱。']

end=['快去睡觉别熬夜.','要一起加油啊.','注意身体多喝热水.','晚安.','总之, 我超喜欢你的.']

print(name,":")
print("当我第一次见到你时,你是如此的"+(random.choice(adj3)))
print("\n")
for i in range(lines):
      for j in range(random.randint(5,10)):
            print(random.choice(text),end='')
      print("\n")

for i in range(2):
      print(random.choice(end))
input()
