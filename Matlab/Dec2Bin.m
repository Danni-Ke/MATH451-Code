function result=Dec2Bin(Decimal)
a=10;
fraction=Decimal-floor(Decimal);

integer = floor(Decimal);

integeresult=[];
fractionresult=".";
%integer
while(integer~=0)
    Remainder=mod(integer,2);
    integer=(integer-Remainder);
    
    % 1
    integer = integer / 2;
    
    integeresult=num2str(Remainder)+integeresult;
end
%fraction
 for i=1:a
    temp=fraction*2;
    if(temp==1)
       fractionresult=fractionresult + "1";
       break;
    elseif(floor(temp)==1)
       fractionresult=fractionresult+"1";
        else
         fractionresult=fractionresult+"0";
    end
        fraction=temp-floor(temp);
 end
  % result=[integeresult,fractionresult];
  result = integeresult + fractionresult;

  disp(result);