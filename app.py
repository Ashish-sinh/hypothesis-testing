import numpy as np 
import streamlit as st 
import scipy.stats as stats 


def hypothesis(ctrl_visitors,
            ctrl_conversions, 
            treatment_visitors, 
            treatment_conversions, 
            confidence_level = 90 or 95 or 99 ):

    try : 
        ctrl_rate = ctrl_conversions / ctrl_visitors
        treatment_rate = treatment_conversions / treatment_visitors

        pooled_std_err = ((ctrl_rate * (1 - ctrl_rate)) / ctrl_visitors +
                        (treatment_rate * (1 - treatment_rate)) / treatment_visitors) ** 0.5

        z_score = (treatment_rate - ctrl_rate) / pooled_std_err

        if confidence_level == 90:
            critical_z = 1.645
        elif confidence_level == 95:
            critical_z = 1.96
        elif confidence_level == 99:
            critical_z = 2.576
                
        if z_score > critical_z:
            st.subheader(" Result : :blue[Treatment Group is Better 📈 ]")
        elif z_score < -critical_z:
            st.subheader("Result : :blue[Control Group is Better 📈 ]")
        else:
            st.subheader("Result : :blue[Indeterminate]") 

    except : 

        st.error('* Your Entered values might be incorrect or Indeterminate (see sample) ') 


st.set_page_config(
    page_title= 'Hypothesis Testing', 
    page_icon= '📊'
) 

st.title('Test Your Hypothesis Here 📋 📈')
st.image("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAARQAAAC3CAMAAADkUVG/AAABs1BMVEX/////6CjMzP/w8PD4+PjGxvnu7u7AwPIAAAD/5gDOzv/GxvL/6yT/6ib+5yj6+vr/7iD/8RsAAJTS0v//GRnm5ubzZmb/Cgr/5xh2dnbAwMD/8xh+fn6SkpK5ubmLi4uhoaHPz8/b29v/9sb/++oAB5OmpqZtbW3Jycm+yPz/+t7/7XD/8qMAHpAAFJLq2TYAIY8AFpH/9b1vb4rwXHH/7GT/87D/6lP/8I2Xk2f/6UaxqFsYLI3fzz7/+NLRw0iBgHBtb3j/8JGkpMx0dJGIiKm4uOScnML6ICbh4u3m6PHBuFHj0zwkNIueml1hZXxJUYJXXX8yPYi5r1aOi2t+fXDVx0WrpF47RodlZWVYWG9DQ1TJy926vtdpcqx2fa+qrsxQWp1RV4A5R4YYLYn//AC0rkpIToPGu0yXlWGIhGkoOIk5RYStqlMmJiZISEgeHh5RUVEGBh0aGi0yMkgNDQBX0tjB7O4Av8iY4OQiIhYrKzbf3/8pKR8iIjYwEiUbPDyAAABYAABHWlrJAwOwAAAAICAfAAAxAAC7AAA8MTFURESDV1ekWFi/Xl7ZYWHng5Ld5Js+AAAXzElEQVR4nO1dC0MaSbZuARGZ6qa6Cbu0KCAJ6CSRxrgmEiDI8FoFaQUENaBonAg42ZnM7n3t3N07s3dn996ZfdyffE9182ieEjQR0C+TiNVNU/X1d75zqqp1KKonHs1O3RiYD8fNfXhXmF/0HnkfPL5BUqakQQ7Ox8emBEh5OhQpD2+SlNHD7FCkPDffdr8/JsxPhiLli4kmZcr8aBhSnkw4KcNI5SaTzyjC/GwITtYnXChfDCGUpxMulKE8ZbJzD8C8fk9KO+gX90rpwFDJ5+k9KXeQlI17UjowO8yEcORIoRHqaBr+akMJZcSMFmGczCTaWEF0B00DY/bVmJOCMCp7NzfFSy9uaU5xQNOQahmOlFcjUtHSCAe9+3wo5GM2z1pIYfdWM4hmhmSFeTwEKaMxH6Qxk3rj3BN9DIuFs4CSABqtuAXEiuXhYmiouQ912+GDaRqxySof2vEkLIieYlKMYvggoOTqOSPkuCQwRTy4SRgehKbZh8OQcrPLpDT+QJmjrEAnROeumNx156RRIsUVaCGTvfB7OI7bscCRYBmhHIktxLI09rY7cjcMt0Z7Y+GDgQ86WU32ZgV1OUQLMGInH2BZj1P2DVo+jWYxO4XynNvv9yYD5TIRit/JBs7TeAqV93YEYdWDO6/XjtmXw5DyctD4ofvLFVVCDM2GOF/Ps1Cm2zGayWQYiCEhfcmS71khIRACBNEtAks5VtwTECKfjRJuHuXfcAISuHNhz3vmv4oU86x5Y6jVyEcvr6RDCgmaEVP9OsFecgFEr1z2PAccUyaFptvaiTRQkBfJW9lN7uICT+Hg6opHBHYQ41uC4wF4Jw65g2/3Agc5C+/MWHxvQ+dsv/tknp16MsSqWw1XBRC9H4TAEHZXztg+JwnuFYQCq72JQz6OSADcMsd2xhHKeyswQrbq3LN4EC67nVkSj8RVQhhnyVuxx894U4F0QHC+sQhV5mwHZSs9WTFvDJOMG3jRP4CwlyPVlNyxnpzgxKr4pSWoPAfJ5gDSl4hC5aokhYTH6ey8Eq56g2gK5Zw7bEZkA2f+snwH6NxbL2bPPeAvmR1vaoctfyV43RkLH7T4095Athcp5tmh4qaJvpzQjMdPBI89u72FwjJB0b+TPthPN86hcTnPSCT4OV5mhfxryTrdoXxnKcaeeYEp9sAdxG4Bp/wZ6S2QkXP5BA4498Fdd3d8qyk2ERIO3GwmxAruHaFznlTnZOPp9Ujpv2+KfM48dJAOePLKHrSMCosc5/fse7MX1Xr00MIlxwMZ7KbTfSbdT0RGwGb9nqClSxpCF1kYd8Z98eVZBcp9ZxBjsFfhbTlfSeKMM4OQz3O+v0pD4gm491guiYNObx+PezlUfd9E/31T9myV3FfsrWte8kkkoJphQnQgOpct75xhLOxmasTR9I4zkwthdn/VDySQ84JcjkYZcYfpdndpIQSksJee0GWKpYVUbpcT8wkgubqZZSCAk4j28Bce4Ctx9taZCVVZvO9+2y8dzl7LUsBU+hRcUEdI4mfTe6wkD1qATEDnuDwWyPBwnk9lQOWCN8SiHFiK7CRARvXLvQSbEg9qJGAeilKUh9iQqEStiQMlNr2YZpzpHKTnpBfqeibDpUFUzNt9jKtOxhJ6w/tXGFDKxVunCIoJ7rr7lETDlrJN9CtqYY5KZh0QPSnoNKkWylwOsWduOni2mwCNcCtCbldAAdL5ip/F2VWSq5LOc7Z8wLIhj8wJkOCBOgSnVrwBDJm0nKqmUMvHVCBCgu5NlqYZnw9ycjmds9DVYOBdFUh5wya4/IWHOEvOzVTTSSSkPFeUKdfjpO+ckN2V6kbk80OJfU7UUl7x4iSXZSq5HIdAxBmMfV4cTPkQE7qwlKuhPYgDcSUvgGxo75sgYhHGwXep1U1MC6u01+8ObZ5V8+UWs8VZKPdRAryDRlke0q9vDyyI9eVzQS/C3nPBvS9wK5CfaOTMkRo/m18V+1QIQ64ZKNBni51matEjntG4wsHdzDHn+5YKF3ibYoWvBHTpJ3fPy+aqASScbVryKW+aBaGshA6ScOsT5QtuL1UJ8d7N1QyyiJsYf5lZqe5V2syWFasQGjmujJG4kkOoLFpoGmc8QvltCtGCx71Ks1WOsADeBGcm9hPOfD9LMW8MNT1u4GGfmhYlOMk7kduL8cqZhRbeCs5Ny955roLowK4QcBNJlyu4vInopDsR2GR8HEa+1WoSbmcihRGLq27xTdKS4YI4AeNh+RCNLb5M64jQEuEee/LJXQ6yMb1noaeSKa+AffkMlChCihRvQdnZwcXpC2bTGehnKVCoXMdpn/WLHvA4aSYScOZwDsxkKhHMcSnmbD+RITeQKZNVMVbMMnkvC/cwGMyyZU7AWWeZCCgVoIEEnmGZEONLJ5mVCraIebANC99KCs3wm1LeX+E4IIFm9pMB5l0OJJHfB1OpTRJrJEDtn99n+0woZFKGL/GpKx7FYA++YiG34NRZEkoMC855LSkukBC9FfDCzIHFtwLGkdwpJ99WMcpwQjYBs7WEJQRUogAPNT975oNAsJwJmUtB9COc9ZEbvym2lm+0UCWkwNRYYKSvQqqcJETQTIjLdIQJe8lUVit9SRlucamBfuv5dNKfsQTeVkNpP0OH9tnAgYAP/Gw29M4H0SJ6LV6wYctumi0HYapSWUnwoJt0KsC5MZYm+WwoAZJhQiEsuA8gjzG8BTHBiq+tpKUF/748xtpssZbZSWHcZdKHPGj1vD8nwy0ZNNCvoMWZNP/Vfl6w+N2MkM4gt8/iO8haNncrNP3ynYfG1QuWrYA9Zso+hKs7Xigy6dxXXIUL+pznDE0HKyzNlL1AAkryUBnToXflXFnoGBBI5ANWp6CaW+3rKOan1DWnPj1JQWx+x58hJWuA82GGK++ELIk3TgZuvI+l360KNN7b/TLPiSxKpMoIL/k9OWJAtGBJuLk3pOgNenOBXEIiQV6PwUEIi27j+aAVOywIfRd3zM+vR0nvjAwjy+6eWaakKiWHcIrLWnzV7D6b4z0+35mfVLbBlRD3BpJnqhJAOOSX14lg0MiCpPUBFPDlmJbs25WRD8YVV6GvFzyAZ11JoZkzf5JOS3aGqwckJTKW/SxOMzi1FBI2vVKpioRsBcOhbEgow9yv2hkX3dYgPz7MQz4V2SSle/wwFZj9HwTJ0KF0kyq46h4jQjhV3/gwxg0jnCIrjX5PAuHNzkRxa7jmekqvMh8q7syONOliLyCRQN3B5VK7FsiynYtEOEnYG2jT4RNh9lp1CkX1rGhRnpOLSGklEfkOvDuQS7H/oHPWcY393o+D63rteq+wx5sei/wiR2bSiA+R+gKthAbYW7htXJeUntUb5tMyKbWEKRsJuxPqNz8dEVxzPaV3SYsybkuX1uDBh1RanxK0mWB2loG/1xNKn5UDXO02P0e3GT09Ojs7O2ueNb94srHxxdNnkHgeXnM1sm+df8v+aa5jtoaXT6ZmXzLyS+ChRpF59uGjRxvXXVdqwQj8yAJtboI2S7ddwsaz50+/ePr0+bOHr149fNi4/Y8ePntF5PDF+kvGbGbM69ec6XTD+iyh5VP5BAwbOJhVCMD88sU6ET5g48n6iyevYNDP4L4//ghjHRzP1s2zzIuXH/MBHpkBkPzs+vqLF0+fPXwqC+B2Bz4AHt8oDbTCCsALvnj28OGNRv2nwjXcpR4QjZBg1p9AIng16kK4Gv22xZQEzDYGb56SU8HU+tNXzyAdjklMfAiu+okos1wQPKcgJTTH/ujRh3KggT9jg+d9rJZoY4N5+fjxNcsiggXKdv2LfDLUn1VpKIY20zXHhNB4SA2kifklu4F8VajB2ni1RP6pkaI1aBaplpMMze8UL28bG3LZ9GRKdozZ9ScvXr5c33j6IdOrQ8r0Xgtfl121Bo31N/MO8sJq1djJ1xopdpPJ3nzb4vsll71OhYmyzlFq9fUGc2N4svH4FQmQx49fvXr1fKgcuvQ1zxsWeTuMzMHD+N8vunj5iG1hzmGlDKY6Keq5xQXKvvjeSi3wcy5eS1oo7fy89usFE0W9n1++sWHdOg4179WG39h4akH9k423WrVaiqeIdCCwlqj3oIEaKe+//ka7QC3xVpd9gVowubRa69L83OH8e8o+b3LMLfMTRMp74GWRhM6cy05RjsM5E3W4MAffO+xWO+U6nHfZKEk6h9SC5vAbB7+05Fiy2SirnXdZKZ4cWnD8tGh3LfKufp8zfrAtHS6arPalpWXDnJVySJZiqHtEIyUvqkEz8/X3yHZsPVxyae3wWuNyjVHmHgzLS2AYV8KgIOUuwETc8irMzVGL2o/fl9GFYYRqj5HB+y6+OUCETTTsh13CSTdBaXcILDi+7tJqX3J88p6MDubVCwudnmJw2W1312ddJq3d1UmK2jVn4u+w/9rUts7Rm1wwLbR/+s6MCLQ2yt7ZCqTc5fzTvZLTOijH3KfuyshA3XutbZxW4W4W9t6Z13pX04+mz6xPXo27g3D1K9HuqNUa+H5HF+9mqe9a7Hv4blptX6EAZ6OybP8pYe0vFEpt/yTdGC0sXXXCHYwf65VGunyFlCYQVwrlDkplboDJjX2CNjM6s0Zni6ZdKJqOFQSNQdu2fNtZ+Y9PghqEFKu1rcHUMWKgqW0aMMiFRwQadRtM7Q2dLYZD5bs0piXdt9/q5rUtl9JqNdblD77wbbPRCwPc0MWWwLDqoiq9/rOIriXdkIBqtdoxUkoHBug7r2yx/XbaqJ+e1htjOiVXhJSFFqudbE9xKDfJbb8z6lWq6WmVSq/SKayGkGJqsZ7JJoU3NFusvyWcSKSo9NOKCJLyUYvVTjQpDnuzxaSbJpzIpKj0MV1DQxIpVuWSy0STMq9ptvxL2KgnAE8hMEYbO4Zy5aK02jEy2g9OyY4FTb3FML83PdMC1e9cmnpKJtl6/o6kZJu60eLQSYZC3GS6/qIeQLJSHNZel+neMqq4ou+mhWbLH8IyFXVPARijh/KxWuGvsNoJ9hRp71xucR0ZVe2kqIzfyhmoRoqruV82uaRobY0Wg25G30mKPvZ76cQaKZrmsv7kkiLvlEottkhDKApSVMbXko/U583N+JlYUmo7paRFrVPpu5Gin9GRU+qkLDZWXiaWFLup0cJHm0JpZB9JKqKdUqyw8F0u07NlRPBBdYqJ19RbHLq2EkUBHTlFK79Fs+AYuE7RjmWdUt9Sh5ZDhVBalaIyri0olKK1D3DhUUefvhvmGy0mnYKTFk+RKjiDYoGy/qYJ9ZTGlrqaOozre5IiSaVJylxtN2RCSWl6ZptQ2kghUlEsZdekMpmkNHdKDUvRfqQQqSieT1+Q6ZhMUppb6o2ZYFejlaSimPHWHpUcI1IMmlYYtO0tGrnFYJ2rH4HUA9pQYmam9XvVmq15GWqJ6ndh5YffNhs1dPa0vaHWIg9N6rpJp5/uT8r0jE4xVOuyoc+FR5CUDvQKH8VOKd/mKB3hQ1zF3ryA/HTcGIVPB3qR0twpVevaKWg32sYMqIYFcokJJGW5uYY2Hx2AFJU0A6rBQXaEJpCUplA0OuPM1aRMt0iFJK6epPzrv93oAD4GupOyqBTKQKQYlVIhJU4vUjT//h83PYYbR3dSmjWKWqfXt5PSabT6aZVSKhrbWE0IB1s6WLTXzzPMR3qvGbRudxw13qTWzGsnb4ujuahIhDKYUloSEITfGCmlA9367rA3vgFHUXWQ0s1ToFY5UjyGwE9c9plvbBFrQSiDktIiFZdjwpRiau5TSNPjAUlRKROQdqHzucBxJsVga4xHXkcZlBRpCa6O+c4fIxtnUhxNobyPN0jR65UUdDNakEqk+djBYufPuo8sKVcvHVA2U63JsPit/DQKmRPHY9IaQWOWrG9dTZCnzSpd43KGxix79GfJV5Ji0Nrqo6F+H1ZFRTGil0khLMT1NQrCryMzpGGmzk0sDIdU0feNN9sd7Z81suspHejQ9ELjcSTra6P+yAiY1s9E4zGoV6LfrU0bjXoIlrXP9EcxOBSJ6Y1GldEYW3sdIY/xfNtYw1Tk9V4fNbJo76mmYbNkR934ek2ciaxN62PRGSAlHjHOHImgCVVE/C4CMoobYyrxSLX2OhyX7Sf8+8aF5tuFML6k2E2NNdoISOBIb4zGxCPjGpACZhsByfznkRGUMhONEn6MkUhEDEf1M7FojPiP8chev3DHA/1jS4phXvHcEtz5qF4fOwqHw/FwjKSXI1G1thYDpcRnjPGw+FlYFYmEZ8KiGFe9XtPLaVldv3D7D5ONLSkuR71FF5MGCf8ZZ6TH/qTUS/xDfhAQdBOLHumjxng0ZlTNkEOSVOK1hwO19e35Xh81wmh/FrLeYhPlByH10oSwDbWnI/XG2NFrPWGJ1Ck1GF+7ahdu/7UQI0uKRtsGk/IbtWtZLbWolxVPGUzH4J9IPNxtwWC6c2EhpnOoyYXVmkN1748iGNmfEGq9fXytxQDB00CE6CISjkmaic00lGIkCaeuHdV0QyrxP9Qu3PZDdiOrlA609FTaKSUtX9d3NfSxyHSU1PCkUIE6fiYak+yFVCfR78RYnMSO0fhZeBqydUwu/o1rtTVaw3zvjxpptPSUr7XMNx6E1MePwrGIMTxTIyUsRmNhYOOzIzEeXjNOQ2KOiWL0dVgfWzuqkaIy/tElr9G2/nKR8SRFfopCTbn+2Nj9MkbWjoyvjd+R0QMpr6NHUUjRr2NHUShX1qZj34TXxEjUGF2bFlXRSP2ZY5VuWSLF4er1UaMNZU/lwsJg1TWnxPoIREh8LT4TJYWKHoo1/VokHl2DMjdmXDuaAT6OYrG4uLYWDotH0dr79DM6h6Z5xS4fNdpQ9HRZLkGtLTuCkosa64UKqU7iMTIPgkQMxgKNRlU8rpKytqr5Pn1M/u1vLVY7lqTIt9Wlm9a3oaVOMR4ZY1FVS4tRWafUKxiJlZZfujKypPTZ4li2wkHN0n9dtZfRtV7pLGBiOptBrbE5un3U+GxxkJtq+v6HX33eLpTeFa2iRdXe8vmv//TfmpYFuJFVSgcaPSWZYkH351/+6vO29deB12hb8fmvH/yosyqtdgxJmQc3+eHBg5sk5cGDP33POzo/auRR7+ni94SSmyblwZ//9JdGBTc+pJBywjQ3/xfdjw8efARSAD/+9XvbspaixuF/VGHQaB2Lcy7b0te6//nhf3/ZwACkdN3iaH/T5w+a1/zxh7/qvuYXXMuLDu0I/vJjm66Jb376+ee//f0f//xFC/7vsw7EOpuuxkzrZX/xz3/8/W8///zTN4oOjMpvVzRI6H/KAC0DoH+wXN2Ne9zjHve4xz3ucY8bxPbWbfdg1LBVOikd11jZPrndvnwsbLd9b6DUhV7naqjt0rEHCCnWGkonjZcTg6iaKu60NmlWqXi8paXQrNKLp6fFwmnj2+14+vQ42snrWGPrgKLibbIonlLHrXOVNNUyKSqWgKcTDVU4LWgKp+RAKQ6CKcUVbI0zjgvykJswpP3HJ7JPxEvw95iSloxO3E1nLRWoQrq4XTyHJk2YAlWdF0on25fq0vEn7PpHgwEiZ+sExL9dpE63iwYqXtymwttbJXLwuBSnTk8gMApb1ElU8S4QycpWnLokr7eLmh1q6/jYED8plLZOixMQR0W4y/Gt4gkMa/u4sBXfuqRK5N5vh+MkOLaKkrektw1ETeraCoEaIuW0SBUK8RJgqwDUnRY1pZ3iVine57PGBiSvHlOn1FbhBIanKcVhrFtF6ni7cEwdgNcU4vFiqZQG4uInJ8VaABWK1EmByKdYhJO3i4X48Tk47mWcSk9E8XK6VSwda+LbhVLxhNz7Yw3wBKRAMFF+MA8DFS4Ut08gVuLqRpouAinbkJ8gVAqFEigqTpIVxFTRc6uDuRlsnYBSiqVC/GQ7rT7Z1pwAFcdbhYL6uARJ+RQoo0oQXprTU/iqCdftAnzWcAI0lLYL20RrW5ITbwNZE+CzEBhw88FJiwUIhOPwiYE6OSUC2FqF8UMEbUGMbEONsqUmjY2c3DBT4jEFRVI67lnyjRNA8tQB1BtgkCT9UnLyDWsOGmd8yP7NyWQU/KTWKoAMQCOnzVw6Bns2HxMKDzgenz29jwyDQhR3XB/3uMc97nGPe9zjHve4Sfw/X3C/HEPXElEAAAAASUVORK5CYII=") 

with st.sidebar : 
    st.image('data:image/jpeg;base64,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')
    st.warning('Enter values and estimate your Hypothesis 📋')
    alpha_value = st.selectbox(label='Enter Confidence level (α)' , options= ['90','95','99'])
    st.error("* :blue[If you don't have values then here is samples for all values :]")
    if st.button('see sample values') : 
        st.info("* control_visitors : :green[7977808]\n * control_conversions : :green[874767] \n * treatment_visitors : :green[989983] \n * treatment_conversions : :green[258231]")


    st.info('* the control group typically represents the existing or current condition (e.g., current website design) \n * while the treatment group represents the new or modified condition (e.g., new website design). \n * The number of visitors in each group and the number of conversions are key metrics used to evaluate the effectiveness of the treatment compared to the control.')
    st.link_button('Source-Code (GitHub)' ,url = "https://github.com/Ashish-sinh/hypothesis-testing")
x , y = st.columns(2) 

with x :
    st.write(':red[• Enter Control]')
    Control_visitors = st.number_input('Enter Value of :blue[Control Visitors]')
    Control_conversions = st.number_input('Enter Value of :green[Control Conversions]')  

with y :
    st.write(':red[• Enter Treatments]')
    Treatment_visitors = st.number_input('Enter Value of :blue[Treatment Visitors]')
    Treatment_conversion = st.number_input('Enter Valuse of :green[Treatment Conversions]') 


a , b = st.columns(2) 


if st.button('Test-Hypothesis 📊') :
    hypothesis(ctrl_visitors = float(Control_visitors) , 
        ctrl_conversions = float(Control_conversions) , 
        treatment_visitors = float(Treatment_visitors) , 
        treatment_conversions = float(Treatment_conversion) , 
        confidence_level = int(alpha_value))

def set_bg_hack_url(url):
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url({url});
             background-size: cover
             
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

set_bg_hack_url("https://static.vecteezy.com/system/resources/thumbnails/008/617/161/small/abstract-gradient-pastel-blue-and-purple-background-neon-pastel-color-template-for-website-or-presentation-free-free-vector.jpg")

st.check_is_dark_mode()