#format(starting from "=talk="): 
## date (blank = next Friday)
## address (blank = B1-501)
## paper info:
### conf/journal/tech.rep.(short name, e.g., INFOCOM'17, Tech.Rep.)
### title
### link
### presenter

def collectInfo():
	global date,addr,conf1,title1,link1,presenter1,conf2,title2,link2,presenter2
	global str_summary
	date = raw_input("data(yy/mm/dd): ")
	addr = raw_input("addr(room # e.g., B1-501): ")
	conf1 = raw_input("1st conf/journal name (short name): ")
	title1 = raw_input("1st paper title: ")
	link1 = raw_input("1st download link: ")
	presenter1 = raw_input("1st presenter: ")
	conf2 = raw_input("2nd conf/journal name (short name): ")
	title2 = raw_input("2nd paper title: ")
	link2 = raw_input("2nd download link: ")
	presenter2 = raw_input("2nd presenter: ")
	# date = "1"
	# addr = "2"
	# conf1 = "3"
	# title1 = "4"
	# link1 = "5"
	# presenter1 = "6"
	# conf2 = "7"
	# title2 = "8"
	# link2 = "9"
	# presenter2 = "0"
	str_summary = """
	date: %s
	addr: %s
	conf1: %s
	title1: %s
	link1: %s
	presenter1: %s
	conf2: %s
	title2: %s
	link2: %s
	presenter2: %s
	"""%(date,addr,conf1,title1,link1,presenter1,conf2,title2,link2,presenter2)
	confirm()

def confirm():
	confirm = raw_input("summary:"+str_summary+"update? (y/n)\n")
	if confirm == "y":
		update()
	elif confirm == "n":
		collectInfo()
	else:
		confirm()

def update():
	str_start = """
	<!DOCTYPE HTML>
	<HTML>
	<font  face="Arial">
	<HEAD>
	<TITLE>MobiNets Seminar</TITLE>
	<style type="text/css">
	#returntop{
		border:1px #ccc solid;
		background:#FFF;
		width:80px;
		height:30px;
		position:fixed;
		_position:absolute;
		line-height:30px;
		text-align:center;
		top:0px;
		left:0px;
		display:none;
		cursor:pointer;
	}
	</style>
	</HEAD>
	<BODY BGCOLOR="#FFFFDE">
	<!-- The back top button-->
	<div id="returntop"><a href="#top">Back Top</a></div>
	<script type="text/javascript">
	var getDiv=document.getElementById('returntop');
	var n=0;
	function scrollEvent(){
		var scrollTop=document.documentElement.scrollTop||document.body.scrollTop;
		if(scrollTop){
			getDiv.style.display="block";
		}else{
			getDiv.style.display="none";
		}
		n=1;
	}
	window.onscroll=scrollEvent;
	if(n==0){
		document.body.onscroll=scrollEvent;
	}
	function getWinSize(){
		var winHeight=window.innerHeight,winWidth=window.innerWidth;
		if(document.documentElement.clientHeight){
			winHeight=document.documentElement.clientHeight;
			winWidth=document.documentElement.clientWidth;
		}else{
			winHeight=document.body.clientHeight;
			winWidth=document.body.clientWidth;
		}
	    var height=winHeight-50;
		var width=winWidth-100;
		getDiv.style.top=height+"px";
		getDiv.style.left=width+"px";
	}
	getWinSize();
	window.onresize=getWinSize;
	</script>
	<!-- The back top button-->
	<div align="center" style="width:840px;margin-left:auto;margin-right:auto;">
	<table style="table-layout: fixed">
	<TD width="220"> 
	 <a href="http://mobinets.org/" alt="Home">
	 <IMG SRC="http://mobinets.org/img/mobinetslogo.gif" alt="Home" width="80%" hspace="5" border="0">
	</a>
	</TD>
	<TD>
	<h1>MobiNetS</h1> 
	<P><STRONG>Mobile, Networked and Smart Computing Group</STRONG>
	<br/>
	<font size="">
	[<a href="http://mobinets.org/people/">people</a>]
	[<a href="http://mobinets.org/seminar/">seminar</a>]
	[<a href="http://mobinets.org/research/">research</a>]
	[<a href="http://mobinets.org/pub/">publications</a>]
	<!-- [<a href="recruit">recruit</a>] -->
	</font>
	</P>
	</TD>
	</table>
	<hr>
	</div>
	<div style="width:840px;margin-left:auto;margin-right:auto;">
	<h3>Latest</h3>
	<b>Time (yymmdd):</b>"""+date+"""
	<br>
	<b>Address:</b> """+addr+""", Main Building, Qingshuihe, UESTC
	<ol>
	"""
	str_new = """
	<li>["""+conf1+"""] <a target="_blank" href=" """+link1+"""">"""+title1+"""</a>, """+presenter1+"""</li>
	<li>["""+conf2+"""] <a target="_blank" href=" """+link2+"""">"""+title2+"""</a>, """+presenter2+"""</li>"""

	hisdate = ""
	newhis = ""
	his = ""
	counter = 0
	copy_flag = 0
	fp = open('index.html')
	for line in fp.readlines():
		if "<li>[" in line and counter<2:
			newhis += line
			counter += 1
		if "Time (yymmdd)" in line:
			tmp = line.split('</b>')
			hisdate = tmp[1]
	fp.close()
	fp = open('index.html')
	for line in fp.readlines():
		if copy_flag == 1:
			his += line
		if "History" in line:
			copy_flag = 1
		
	fp.close()

	str_history = """
	</ol>
	<h3>History</h3><ul>
	<li>%s<br>
	<ul>
	%s
	</ul>
	</li>
	%s
	""" %(hisdate,newhis,his)
	# print hisdate
	html = str_start+str_new+str_history;
	fo = open("index.html", "w")
	fo.write(html)
	fo.close()

collectInfo()