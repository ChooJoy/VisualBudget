 $(function() {

	

            new BubbleTree({
                data: data,
                container: '.bubbletree',
                bubbleType: 'donut',
                bubbleStyles: {
                    'fb': {                                              //taxonomy
                        'all': {                                        //name of the node/child
                            // color: '#9900cc',                       //color of the bubble if you like to set it here
                            icon: 'bubbletree/styles/icons/money.svg' //icon url
                        },
                        'gov': {

                            icon: 'bubbletree/styles/icons/unemployment.svg'
                        },
                        'sport': {

                            icon: 'bubbletree/styles/icons/sports.svg'
                        },
                        'youth': {

                            icon: 'bubbletree/styles/icons/family.svg'
                        }
                    },
	        tooltip: {
		qtip: true,
		delay: 800,
		content: function(node) {
		return [node.label, '<div class="desc">'+(node.description ? node.description : 'No description given')+'</div><div class="amount">£ '+node.famount+'</div>'];
				}
			}
		}
            });
        });



