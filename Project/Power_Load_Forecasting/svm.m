filename = 'data/processed/hourWeather.csv';
x = csvread(filename);
filename = 'data/processed/hourLoad.csv';
y = csvread(filename);
y = y(:,2);
allSet = [x y];

num = 5;
[M,N]=size(allSet);
indices=crossvalind('Kfold',M,num);

res = zeros(2000,4);
best_co = 0;bset_mse = 10^7;
cnt = 1;
for log2c = 8.5:0.5:11
    for log2g = -10:0.5:8
        cmd = ['-c ', num2str(2^log2c), ' -g ', num2str(2^log2g) , ' -s 3 -p 10 -t 2'];
        mse = 0;
        sum_co=0;
        for i = 1:num
            test = (indices==i);
            testSet = allSet(test,:);
            trainSet = allSet(~test,:);
            testx = testSet(:,1:end-1);testy = testSet(:,end);
            trainx = trainSet(:,1:end-1);trainy = trainSet(:,end);
            model = svmtrain(trainy,trainx,cmd);
            [py,acc,d] = svmpredict(testy,testx,model);
            sum_co = sum_co + acc(3);
            mse = mse + acc(2);
        end
        disp("------------------");
        disp(cnt);
        res(cnt,:)=[log2c log2g sum_co/num mse/num];
        cnt = cnt+1;
        if (best_co<sum_co/num)
            best_mse = mse/num; bestc = 2^log2c; bestg = 2^log2g;best_co = sum_co/num;
        end
    end
end

%那么程序 为  
fid=fopen('res1.csv','w');  
[b1 b2]=size(res);  
for i=1:b1    
    for j=1:b2  
       fprintf(fid,'%f,',res(i,j));  
    end  
    fprintf(fid,'\n');  
end  
fclose(fid); 

disp("-------");
disp(best_mse);
disp(best_co);
disp(bestc);
disp(bestg);


    
