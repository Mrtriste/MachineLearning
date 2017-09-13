%[ptesty,tmse,d] = svmpredict(testy,testx,model);
%display('预测数据');
%ptesty

filename = 'data/processed/hourWeather.csv';
x = csvread(filename);
filename = 'data/processed/hourLoad.csv';
y = csvread(filename);
y = y(:,2);

allSet = [x y];
len = length(allSet);
%disp(allSet(1:4,:));

%len = 20
%a = zeros(20,2);
%a(:,1) = (1:1:20)';
%a(:,2) = 1

index = randperm(len)';
trainLen = int32(len*0.6);
validLen = int32(len*0.2);

trainSet = allSet(index(1:trainLen),:);
validSet = allSet(index(trainLen+1:trainLen+validLen),:);
testSet = allSet(index(trainLen+validLen+1:end),:);

x = trainSet(:,2:end-1);
y = trainSet(:,end);
x = zscore(x);

%disp(x(1:5,1:end));

c = sprintf('reteyft %f\n',0.1)

model = svmtrain(y,x,'-s 3 -t 2 -c 0.1 -g 1 -p 0.01');
[py,mse,d] = svmpredict(y,x,model);
