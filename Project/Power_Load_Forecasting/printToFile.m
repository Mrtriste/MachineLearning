function [output_args] = printToFile(filename,res)

fid=fopen(filename,'w');  
[b1 b2]=size(res);  
for i=1:b1    
    if sum(res(i,:))==0
        break
    end
    for j=1:b2  
       fprintf(fid,'%f,',res(i,j));  
    end  
    fprintf(fid,'\n');  
end  
fclose(fid); 

end

