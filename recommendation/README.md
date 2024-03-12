Two environments need to be configured before running the following code:<br>
1.nltk<br>
Run the following python code:

import nltk<br>
nltk.download('wordnet')<br>
nltk.download('punkt')<br>
nltk.download('vader_lexicon')

If the above code fails to run, you can try to manually download the relevant dataset and place it in the appropriate location.<br>
For example, after creating a folder named wordnet under the path (D:\nltk_data\corpora), you can download and unzip the wordnet dataset, and finally move the dataset to that folder.

2.KAFKA<br>
The specific process of building kafka in local windows environment is as follows:<br>
First, install the kafka-python package via "pip install kafka-python -i https://pypi.tuna.tsinghua.edu.cn/simple".<br>
Secondly, download kafka via "http://mirrors.cloud.tencent.com/apache/kafka/".<br>
Next, extract the kafka files into a folder. You need to be careful not to set a very long path, otherwise it will generate an error. Enter the folder, open a cmd window for each of the following commands, and don't close it even after success.<br>
 (1) zookeeper-server-start.bat ... \... \config\zookeeper.properties <br>
 (2) kafka-server-start.bat ... \... \config\server.properties # load configuration <br>
 (3)kafka-console-producer.bat --broker-list 127.0.0.1:9092 --topic test #Start the producer <br>
 (4) kafka-console-consumer.bat --bootstrap-server 127.0.0.1:9092 --topic test --from-beginning #Start the consumer on port 9092. <br>
Finally, run a couple of simple demos you can find on the web to check if the installation was successful.
