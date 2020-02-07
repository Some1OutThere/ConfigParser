from configparser import ConfigParser
config=ConfigParser()
config['123456789']={
	"Name":"Rahul R",
	"Address":"#6, Sholingnallur, Chennai",
	"Phone":"9847467226",
	"DOB":"22-05-1995",
	"Balance":"$67383"
	}
config['123456790']={
	"Name":"Vinoth K",
 	"Address":"#21, Navalur, Chennai",
	"Phone":"9847467456",
	"DOB":"04-06-1995",
	"Balance":"567843"
	}
config['123456791']={
	"Name":"Sangeetha",
	"Address":"#66, Perungulathur, Chennai",
	"Phone":"9847464466",
	"DOB":"15-06-1989",
	"Balance":"5004"
	}
config['123456792']={
	"Name":"Ameer",
	"Address":"#15, Perumbakkam, Chennai",
	"Phone":"9847464467",
	"DOB":"11-11-1991",
	"Balance":"3509"
	}
f=open("account.ini","w")
config.write(f)
f.close()
