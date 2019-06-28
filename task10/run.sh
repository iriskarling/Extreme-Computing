OUTPUT_DIR=/user/${USER}/assignment/task10
OUTPUT_FILE=output.out

# Hadoop won't start if the output directory already exists
hdfs dfs -rm -r $OUTPUT_DIR

hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
  -D mapreduce.job.name=${USER}_demo_word_count \
  -D stream.num.map.output.key.fields=3 \
  -D mapred.reduce.tasks=1 \
  -input /data/large/imdb/title.basics.tsv \
  -input /data/large/imdb/name.basics.tsv \
  -output $OUTPUT_DIR \
  -mapper mapper.py \
  -reducer reducer.py \
  -file mapper.py \
  -file reducer.py

  hdfs dfs -cat ${OUTPUT_DIR}/part-* | head -n 20 > $OUTPUT_FILE
  cat $OUTPUT_FILE
