%[ptesty,tmse,d] = svmpredict(testy,testx,model);
%display('棰勬祴鏁版嵁');
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

x = trainSet(:,1:end-1);
y = trainSet(:,end);

vx = validSet(:,1:end-1);
vy = validSet(:,end);
%x = zscore(x);

% mse = 10^7;
% for log2c = -10:0.5:3
%     for log2g = -10:0.5:3
%         % -v 交叉验证参数：在训练的时候需要，测试的时候不需要，否则出错
%         cmd = ['-v 3 -c ', num2str(2^log2c), ' -g ', num2str(2^log2g) , ' -s 3 -p 0.4 -t 3'];
%         cv = svmtrain(y,x,cmd);
%         if (cv < mse)
%             mse = cv; bestc = 2^log2c; bestg = 2^log2g;
%         end
%     end
% end


model = svmtrain(y,x,'-s 3 -t 2 -c 512 -g 0.031 -p 10');
[py,acc,d] = svmpredict(vy,vx,model);
disp("----")
disp(acc(3)) %accuracy, mean squared error, correlation coefficient












