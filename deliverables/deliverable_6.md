# Implementation 2

## 1. Introduction

StockInfinity aims to provide transparent stock information to users through multiple platforms to deliver a seamless experience and an exceptional level of accessibility. It is difficult to find a financial application that is not littered with unnecessary information. Many of the current stock application powerhouses have had incidents in which they were exposed for ingenuine practices which have large impacts on an investor’s financial well being. For those who need honest and uncluttered information about their favorite stocks, Stock Infinity can bridge the gap that larger firms and companies have been incapable of providing. Our product offers a friendly interface that allows you to see the information that you need without the extra fluff. You can be confident that our product will deliver the information you need for your financial future without fail. A simple, honest, and comprehensive application that allows both novice and expert investors to view information on their preferred stocks without having to sift through unnecessary information or worry about conflicting interests of shareholders affecting their access to information.

While StockInfinity is still in its early development stages, our web application is available to select any and all users for local testing. This web app features a simple user interface with user experience as a main focal point, the ability to search for any publicly traded stock within the U.S., and the ability to favorite stocks after creating an account. User profiles allow us to control notification timing, whether that be based on daily notifications or price updates on a selected interval. No longer do we need to rely on biased information! Now, everyone can find unbiased information on the stocks that they want to purchase.

Project repo: [Github link to StockInfinity](https://github.com/davidknight00/finance_app)

## 2. Implemented Requirements
**Requirement**: As a long time stock trader, I want to be able to connect the change in a stock with a reason from a news article so I can understand the full picture. \
**Issue**: https://github.com/davidknight00/finance_app/issues/33 AND https://github.com/davidknight00/finance_app/issues/30 \
**Pull request**: https://github.com/davidknight00/finance_app/pull/51 \
**Implemented by**: David Knight, Jack Shanley, Nate Chan \
**Approved by**: Alex Poole

## 3. Tests
**Test Framework**: DJango unittest \
See our tests [here](https://github.com/davidknight00/finance_app/tree/master/stockInfinity/stockInf/tests) \
An example test case that we created was testing that the correct view was being displayed for POST requests. This view can be seen [here](https://github.com/davidknight00/finance_app/blob/master/stockInfinity/stockInf/views.py#L16-L53) and the test for this view can be found [here](https://github.com/davidknight00/finance_app/blob/master/stockInfinity/stockInf/tests/test_views.py#L24-L34) These set of tests ensure that a ticker (such as TSLA) returns the correct html and response code, and tickers that do not exist (such as OMG) return the 404 page. 

**![StockInfinity unit test](./deliverable_images/unittest_samplerun.png)**

## 4. Demo
Link to video: [here](https://youtube.com/shorts/mbZx9SqsiXA?feature=share)

## 5. Code Quality
We adopted the PEP8 Style Guide. The full guide can be seen [here](https://peps.python.org/pep-0008/). Using the `pycodestyle` library, we are able to ensure the code that we right is complient to the current style guide for Python. 

## 6. Lessons Learned
After the last implementation, we got a majority of the app built. The last step was making sure we made the web app look good so formatting was a big focus. We also wasnted the relevant stories to be implemented so useres can make connections to price changes. We learned this time that we should take less on and make sure that we do it right instead of doing a lot of work poorly.
