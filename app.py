from flask import Flask, render_template, request

app = Flask(__name__)

# Store all bids
bids = {}

# ASCII Art Logo
logo = r'''
                             ___________
                             \         /
                              )_______(
                              |"""""""|_.-._,.---------.,_.-._
                              |       | | |               | | ''-.
                              |       |_| |_             _| |_..-'
                              |_______| '-' `'---------'` '-'
                              )"""""""(
                             /_________\\
                           .-------------.
                          /_______________\\
'''

@app.route('/', methods=['GET', 'POST'])
def auction():
    message = ""
    view_result = False
    sorted_bidders = []
    highest_bidder = None
    highest_bid = None

    if request.method == 'POST':
        if 'view' in request.form:
            view_result = True
            sorted_bidders = sorted(bids.items(), key=lambda item: item[1])
            if sorted_bidders:
                highest_bidder, highest_bid = sorted_bidders[-1]
        else:
            name = request.form['name']
            bid_price = int(request.form['bid'])
            bids[name] = bid_price
            message = f"Thank you {name}, your bid of ${bid_price} has been submitted!"

    return render_template('index.html', logo=logo, message=message, 
                           view_result=view_result, sorted_bidders=sorted_bidders, 
                           highest_bidder=highest_bidder, highest_bid=highest_bid)

if __name__ == '__main__':
    app.run(debug=True)
