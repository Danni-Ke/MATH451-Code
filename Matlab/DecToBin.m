function ansStr = DecToBin(src)
% handle the negative case
neg = 0;
if (src < 0)
    src = src * -1;
    neg = 1;
end
% obtain integer part and fraction part from the source
i = floor(src);
f = src - i;
% variables declaration
iStr = "";
fStr = "";
count = 0;
% calculate the integer
while (i > 1)    
    if (mod(i, 2)) == 0
        iStr = "0" + iStr;
    elseif (mod(i, 2)) == 1
        iStr = "1" + iStr;
    end
    i = floor(i/2);
end
iStr = "1" + iStr;
% calculate the fraction
while (f ~= 1)    
    % end case
    if (count > 16)
        break;
    end
    f = f * 2;
    if (floor(f) == 0)
        fStr = fStr + "0";
    elseif (floor(f) == 1)
        fStr = fStr + "1";
        % another end case
        if (f == 1)
            break;
        end
        f = f - 1;
    end
    count = count + 1;
end
% combine two parts and handle the negative case
ansStr = iStr + "." + fStr;
if (neg == 1)
    ansStr = "-" + ansStr;
end
% display answer
disp(ansStr);
end