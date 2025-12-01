from pyspark import SparkConf, SparkContext
nomappli = "p1"
config = SparkConf().setAppName(nomappli)# crée un objet de configuration Spark 
sc = SparkContext(conf=config) #  crée le contexte Spark
data = sc.textFile("file:///root/arbres.csv") # lire file et creer RDD
print("\n\n --- size = ",data.count()," --- \n\n")