#include <boost/algorithm/string.hpp>
#include <boost/tokenizer.hpp>
#include <vector>
#include <iostream>
using namespace std;


bool compare_field(int field_num, char sep, char* value, char* line){
    if(field_num<0){
        return false;
    }
    //The char* line should have a null character ('\0') at the end
    int i =0;
    //field_counter helps us track in what field we currently are
    int field_counter = 0;
    //Once we located a field, we compare char by char,using char_cnt as an index
    int char_cnt =0;
    while(line[i]!='\0'){
      if(line[i]==sep){
        //Everytime we encounter a separator, we are entering a new field
        field_counter +=1;
        i+=1;
        continue;
      }
      if(field_counter==field_num){
        //If we are in the right field, we start comparing char by char
        while(value[char_cnt]!='\0'){
          if(value[char_cnt] != line[i]){
            return false;
          }else{
            i++;
            char_cnt++;

          }

        }
        //If we break from this whileloop, it means the comparison is true
        return true;
      }

      i++;
    }
      return false;
}


int main(){
	
	string table_str;
	while(getline(cin, table_str)){
		size_t len = table_str.size();
                char buff[len+2];
		strncpy(buff, table_str.c_str() , len);
		buff[len] = '\n';
		buff[len+1] = '\0';
		//cout << table_str;
		if( compare_field(0, ',', "1", buff) ){
			cout <<  buff;// << "\n";
		}
			
	
	}
	
	//cout <<  "\noutput:\n";

	//cout << table_str;
		
	
	/*	
	cout <<  table_str;
	
	cout << "\n\n Filtering starts here!\n\n";
	
	size_t len = table_str.size(); 
	char buff[len+1];
      	char result[len+1];
      	int result_index =0;
      	strncpy(buff, table_str.c_str() , len);
      	//auto len = bl.length();
      	buff[len] = '\0';

      	char* line = strtok(buff,"\n");

      	while(line !=NULL){
        	auto line_len = strlen(line);
        	if( compare_field(0, ',', "1", line) ){
          		//If the line we are currently looking at passes the filter, wecopy it to the result buffer
          		strncpy(result + result_index, line , line_len ); // We don't want to copy the null character
          		//Add the '\n' return character 
          		//line[line_len+1] = '\n';
          		result_index += line_len;
          		result[result_index] = '\n';
          		result_index +=1;
        	}
        line =strtok(NULL,"\n");
      	}
      	result[result_index] = '\0';
	
	cout <<  result ;
	*/
	return 0;
	
}
