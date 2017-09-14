filename = 'data/processed/hourWeather1.csv';
x = csvread(filename);
filename = 'data/processed/hourLoad.csv';
y = csvread(filename);
y = y(:,2);

len = length(y);
index = randperm(len)';
trainLen = int32(len *0.85);
trainx = x(index(1:trainLen),:);
trainy = y(index(1:trainLen),:);
testx = x(index(trainLen+1:end),:);
testy = y(index(trainLen+1:end),:);

%1 time; 2 wet; 3 avrtemp; 4 h_temp; 5 l_temp;
%6 rain; 7 wind; 8 air pressure; 9 sun; 10 temp^2
choose = [1 2 3 7 8];
x = x(:,choose(:));

mm = mean(trainx);
vv = std(trainx);
trainx = (trainx-mm)./vv;
testx = (testx-mm)./vv;

%x = zscore(x);

res = zeros(2000,3);
best_mse = 10^7;
cnt = 1;
for log2c = 8.5:0.1:10
    for log2g = -1.5:0.25:-0.5 %0.025:0.003:0.05
        c = 2^log2c;g = 2^log2g;
        cmd = ['-c ', num2str(c), ' -g ', num2str(g) , ' -s 3 -p 10 -t 2 -v 10'];
        mse = svmtrain(trainy,trainx,cmd);
        disp("------------------");
        disp(cnt);
        res(cnt,:)=[log2c log2g mse];
        %fid=fopen('jindu.csv','w'); 
        %fprintf(fid,'%f,',cnt); 
        %fclose(fid); 
        cnt = cnt+1;
        if (mse<best_mse)
            best_mse = mse; bestc = c; bestg = g;
        end
    end
end

filename = 'output/12378_1.csv';
prefilename = 'output/12378predict_1.csv';
finalfilename = 'output/12378final_1.csv';
printToFile(filename,res);
res = csvread(filename);
res = sortrows(res,3);
printToFile(filename,res);

precise = zeros(100,4);
for i = 1:10
  c = 2^res(i,1);g = 2^res(i,2); 
  cmd = ['-c ', num2str(c), ' -g ', num2str(g) , ' -s 3 -t 2 -p 10'];
  model = svmtrain(trainy,trainx,cmd);
  [py,acc,d] = svmpredict(testy,testx,model);
  precise(i,:) = [res(i,1) res(i,2) acc(2) acc(3)];
end
printToFile(prefilename,precise);

precise = csvread(prefilename);
precise = sortrows(precise,3);
c = 2^precise(1,1);g = 2^precise(1,2);
cmd = ['-c ', num2str(c), ' -g ', num2str(g) , ' -s 3 -t 2 -p 10'];
model = svmtrain(trainy,trainx,cmd);
[py,acc,d] = svmpredict(testy,testx,model);
final = [testx testy py];
printToFile(finalfilename,final);

