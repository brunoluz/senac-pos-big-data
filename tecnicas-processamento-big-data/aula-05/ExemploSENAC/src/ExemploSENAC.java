
package SENAC;

import java.io.*;
import java.util.*;
import java.util.Random;
import java.text.*;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.fs.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.*;
import org.apache.hadoop.util.*;


public class ExemploSENAC extends Configured implements Tool 
{          
    public static void main (final String[] args) throws Exception {   
      int res = ToolRunner.run(new Configuration(), new ExemploSENAC(), args);        
      System.exit(res);           
    }   

    public int run (final String[] args) throws Exception {
      try{ 	             	       	
          
        }
        catch ( Exception e ) {
            throw e;
        }
        return 0;
     }
 
    public static class MapSENAC extends MapReduceBase implements Mapper<LongWritable, Text, Text, Text> {
            
      public void map(LongWritable key, Text value, OutputCollector<Text, Text> output, Reporter reporter)  throws IOException {                  
        
      }        
    }
 
    
    public static class ReduceSENAC extends MapReduceBase implements Reducer<Text, Text, Text, Text> {       
       public void reduce (Text key, Iterator<Text> values, OutputCollector<Text, Text> output, Reporter reporter) throws IOException {  
          

    }
}

   public static class MapSENACMaior extends MapReduceBase implements Mapper<LongWritable, Text, Text, Text> {

      public void map(LongWritable key, Text value, OutputCollector<Text, Text> output, Reporter reporter)  throws IOException {
        

            
     }
}

    public static class ReduceSENACMaior extends MapReduceBase implements Reducer<Text, Text, Text, Text> {   
       public void reduce (Text key, Iterator<Text> values, OutputCollector<Text, Text> output, Reporter reporter) throws IOException {     
               
  }

}
}


