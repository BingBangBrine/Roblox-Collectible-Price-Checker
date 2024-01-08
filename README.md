Opens the page of the item you are looking to buy once you can afford it.

Steps to use:
1. Getting the cookie
   - You need to have a cookie in order to authenticate yourself, otherwise the price will say 0.
   - To get a cookie, use any valid roblox account (you can just make a new one) and on the chrome browser go to inspect element (F12).
   - Go to the application tab. Within this, go to the menu which says storage, where you will find cookies. Use the dropdown in this to find https://www.roblox.com and click this. Now you will see the cookies that are being used on this site.
   - Find the cookie which is named ".ROBLOSECURITY" and find its value which should look something like: "_|WARNING:-DO-NOT-SHARE...". This is the cookie you will enter into the cookie.txt file.
   - This is basically your login credential which allows you to not have to sign in every time. Like it says, do not share it, and do not use it on any public IDE or public coding software. Anyone who has it can get into your account.
   - Because of this, it is preferred that you do not use a cookie from your own personal account, but from an account which you do not care about, like a new one (which is free to make).
   - Make sure that if you make a new account, do it in an incognito tab so that the cookie will not expire immediately. So, once you have copied the cookie, do not log out, just close the tab of the incognito window.

2. Selecting the item you want
   - Once you have your cookie, now you must find the item that you want. You will need the item ID.
   - By default the program has The Classic ROBLOX Fedora id. You may not want this hat, so just navigate to your item of choice, look in the url where it says "/catalog/someItemID/itemName" and copy the part with the numbers.
   - Replace this with the itemID variable.

3. Setting your balance/Max price
   - Now you have the cookie and the item you want. All that is left is selecting how much robux you have available to spend on this item.
   - Simply enter your budget into the "balance" variable.
  
4. Delay
   - You do not have to change the delay, however you may want a lesser or greater delay.
   - By default it is set to a one second delay per search, meaning that if the search takes less than one second, it will wait for the remaining time of that second. This means each search will take at least that time.
   - If the delay is too small, you may get errors.
