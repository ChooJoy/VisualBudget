$(function(){


function resize(str, nMin)
{
	var result ="";

	var num='';
	var find="01234567890.";
	for(var ii=0;ii<str.length;ii++){
		if(find.search(str[ii]) != -1){// Число
			num+=str[ii];
			//alert(str[i]+"!=-1");
		}
		else{ // Не число
			if(num.length!=0){
				//alert(num);
				result+=(num/nMin).toFixed(1);
				num='';
			}
			result+=str[ii];
		}
	}
	
	return result;
}

function getClientWidth()
{
  return document.compatMode=='CSS1Compat' && !window.opera?document.documentElement.clientWidth:document.body.clientWidth;
}
 
function getClientHeight()
{
  return getClientWidth()/2;
}

	var a = JSON.stringify(map_path);
	var b = JSON.parse(a);
    var color = '';

    css_class = 'no';    

	data_arr = new Array(83);

    var i = 0;
	for (key in b) {
         for (var num_elem = 0; num_elem < region_data.length; num_elem++) {          
            if (region_data[num_elem]['code_iso'].substr(3, region_data[num_elem]['code_iso'].length) == key) {
        		data_arr[i] = new Array(resize(b[key].path, 1500/getClientWidth()*1.6), b[key].name, b[key].id, region_data[num_elem]['capital'], region_data[num_elem]['flag'], region_data[num_elem]['num_reg_doc'], region_data[num_elem]['num_loc_doc'], region_data[num_elem]['code_rus']);
            }
         }
         i++;
    }


	var r = Raphael(document.getElementById("map-column"), getClientWidth()*0.7, getClientHeight()*0.8),
		attributes = {},
		arr = new Array();

	i = 0;	
	for (i=0; i<data_arr.length;i++) {

        var css_class = 'no';
        if (data_arr[i][5] + data_arr[i][6] > 10) {css_class = 'many';}
        if ((data_arr[i][5] + data_arr[i][6] > 0)&&(data_arr[i][5] + data_arr[i][6] < 10)) {css_class = 'middle';}

        url = '/region/' + data_arr[i][7];		

		var obj = r.path(data_arr[i][0]);
        obj.node.setAttribute("class", css_class);

        obj.url = url;
        
        attributes = {
            fill: '#ff0',
            stroke: '#000',
            'stroke-width': 1,
            'stroke-linejoin': 'round',
        }

		obj.attr(attributes);


		obj
		.hover(function(){
			this.animate({
                opacity: 0.4,
                stroke: '#000',
				'stroke-width': 1,			    
			}, 300);            
		}, function(){
			this.animate({
                opacity: 1,
				'stroke-width': 1,     
			}, 300);
		}).click(function() {window.location.href=this.url; });
      

		$(obj.node).qtip({ 
                content: { 
                    text: 'Административный центр: <b>' + data_arr[i][3] + '</b><img src="http://choojoy.ru/' + data_arr[i][4] + '" style="float: right;"><br><br>Региональных бюджетов: ' + data_arr[i][5] + '<br>Муниципальных бюджетов: ' + data_arr[i][6], 
                    title: { 
                        text: data_arr[i][1]
                    }
                },		
	            style: {
	                background: '#fff',
	                color: '#333',
	                border: { width: 1, radius: 0, color: '#666' }
	            },
	            position: {
			        target: 'mouse',
                    adjust: { mouse: true },
	                corner: {
	                    tooltip: 'bottomLeft'
	                }
	            },
                hide: { 
                    when: 'mouseout', 
                    fixed: true 
                }
	        });

	}
});

