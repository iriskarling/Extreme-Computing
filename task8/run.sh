OUTPUT_DIR=/user/${USER}/assignment/task8
OUTPUT_FILE=output.out


# Hadoop won't start if the output directory already exists
hdfs dfs -rm -r $OUTPUT_DIR
hdfs dfs -rm -r /user/${USER}/tasks/output


hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
  -D mapreduce.job.name=${USER}_demo_word_count \
  -D mapred.reduce.tasks=1\
  -D stream.num.map.output.key.fields=2 \
  -input /data/large/imdb/title.basics.tsv \
  -input /data/large/imdb/title.ratings.tsv \
  -output /user/${USER}/tasks/output \
  -mapper mapper.py \
  -reducer reducer.py \
  -file mapper.py \
  -file reducer.py


  hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
    -D mapreduce.job.name=${USER}_demo_word_count \
    -D mapred.reduce.tasks=1\
    -D stream.num.map.output.key.fields=2 \
    -input  /user/${USER}/tasks/output \
    -output  $OUTPUT_DIR  \
    -mapper mapperb.py \
    -reducer reducerb.py \
    -file mapperb.py \
    -file reducerb.py

    hdfs dfs -cat ${OUTPUT_DIR}/part-* | head -n 20 > $OUTPUT_FILE
    cat $OUTPUT_FILE
