from tobrot.sample_config import Config
#Fill your all data, read readme for reference

class Config(Config):
	TG_BOT_TOKEN= "1224966566:AAHChjFmvmqG6532VXTU1sI37pQkKoSBhLs"
	APP_ID = 1751973
	API_HASH = "1d27e36489924b52c985879bccaf861d"
	OWNER_ID = "614220961" #ID of bot owner
	AUTH_CHANNEL = [-1001324383627]
	DESTINATION_FOLDER = "HelloMan" #Name of your folder read readme
	RCLONE_CONFIG = """type = drive\nscope = drive\ntoken = {"access_token":"ya29.a0AfH6SMCDXM4PKg_zHxeo5b8dr9RZ4NH_hOgpgMd23MP1_zq-9YTbzxUKSVFOMXq0pxrBsuOhVGq1PuKLTSnvTIaICQDRNqZxkoaIDtHyK40oMnIq9cUfTdub5Y-MywLKsfQVvShCcOZ8JzTXino_kGNjpOsPNEE7fNVu","token_type":"Bearer","refresh_token":"1//0d3LMc8GmH948CgYIARAAGA0SNwF-L9IrThGqybbE1Q-o-Ho-aopNQ4ODZuaIkxgKwL24ahJgcGxzsI8vxiU3qIebWcO8aEPZXlQ","expiry":"2020-08-22T16:57:35.689120481Z"}"""
	#fill taking reference of this config, dont remove """ from both side of the RCLONE_CONFIG variable 
