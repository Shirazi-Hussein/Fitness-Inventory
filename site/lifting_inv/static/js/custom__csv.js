
$(document).ready(function(){

	let first = true;
	  console.log('Script running')
	  let barbell_item = document.getElementById('barbell-item');
	  let plate_item = document.getElementById('plate-item');





	$.ajax({
	type : "GET",
	  url: "../static/js/combined_csv.csv",
	  dataType: "text",       
	  success: function(response)  
	  {
		let items = $.csv.toObjects(response);
		let data = JSON.parse(JSON.stringify(items));
		// var total_html = "";
		if(first==true){
			PrintItem(items, data)
			console.log("In truuuu")
			first=false
		}
		barbell_item.addEventListener('click',()=>{
			PrintItem(items, data, 'Barbell', 'Barbells')	
		})

		
		plate_item.addEventListener('click', ()=>{
			PrintItem(items, data, '   Plate', 'Plates')	
		})
		
  		// $('.load_csv').append(total_html);

	  } ,
	  fail : function(console){
		  console.log('Erro')
	  }
	});

	function PrintItem(items, data, c_item_type, s_item_type){
		let total_html = "";

		if(c_item_type && s_item_type){
			let lower_c  = c_item_type.toLowerCase();
			let lower_s = s_item_type.toLowerCase();
			$.each( items , function(i, item) {
				let temp_s = data[i].p_type.toLowerCase();
				temp_s = temp_s.trim();

				if ((data[i].stock === "In stock" || data[i].stock === "In Stock") && (temp_s===lower_c || temp_s===lower_s) ) {
					total_html += '<div class="col-md-4 col-xs-6">'+
					'<div class="product">'+
						'<a href="'+ data[i].url +'" target="_blank">'+
							'<div class="product-img">'+
								'<img src="'+ data[i].img_url +'" alt="'+ data[i].p_title  +'">'+
							'</div>'+
						'</a>'+
						'<div class="product-body">'+
							'<p class="product-category">'+ data[i].company +'</p>'+
							'<h3 class="product-name"><a target="_blank" href="'+ data[i].url +'">'+ data[i].p_title +'</a></h3>'+
							'<h4 class="product-price">'+ data[i].price +'</h4>'+
						'</div>'+
					'</div>'+
				'</div>';
								
								 
				}
				 
			 });
			 

		}
		else{
			console.log('c_type is not given')
			$.each( items , function(i, item) {
			if (data[i].stock == "In stock" || data[i].stock == "In Stock" ) {
					total_html += '<div class="col-md-4 col-xs-6">'+
								 '<div class="product">'+
									 '<a href="'+ data[i].url +'" target="_blank">'+
										 '<div class="product-img">'+
											 '<img src="'+ data[i].img_url +'" alt="'+ data[i].p_title  +'">'+
										 '</div>'+
									 '</a>'+
									 '<div class="product-body">'+
										 '<p class="product-category">'+ data[i].company +'</p>'+
										 '<h3 class="product-name"><a target="_blank" href="'+ data[i].url +'">'+ data[i].p_title +'</a></h3>'+
										 '<h4 class="product-price">'+ data[i].price +'</h4>'+
									 '</div>'+
								 '</div>'+
							 '</div>';
							
			}
			 
		 });
	

		}
	

		$('.load_csv').empty();
		$('.load_csv').append(total_html);
	  }

  });