% a = zeros(20,3);
% a(:,1) = (1:1:20);
% a(:,2) = (10:10:200);
% a(:,3) = (100:100:2000);
% 
% [M,N]=size(a);
% indices=crossvalind('Kfold',M,10)
% for i = 1:10
%     test=(indices==i);
%     testSet = a(test,:)
%     disp("----")
%     trainSet = a(~test,:)
%     disp("***")
%     
% end

% %比方说 矩阵A 为  
% A=[1.3 2.4 3.5;4.7 5.8 6.9];  
% %那么程序 为  
% fid=fopen('A1.csv','w');  
% [b1 b2]=size(A);  
% for i=1:b1    
%     for j=1:b2  
%        fprintf(fid,'%f,',A(i,j));  
%     end  
%     fprintf(fid,'\n');  
% end  
% fclose(fid); 

% fid=fopen('norm1.csv','w');  
% [b1 b2]=size(res);  
% for i=1:b1    
%     for j=1:b2  
%        fprintf(fid,'%f,',res(i,j));  
%     end  
%     fprintf(fid,'\n');  
% end  
% fclose(fid); 





