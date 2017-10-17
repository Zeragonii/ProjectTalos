<!DOCTYPE HTML!>
<html>
	<head>
		<title>TSS HomePage</title>
		<meta charset=" UTF-8">
		<link rel="stylesheet" href="style.css">
        	<script type="text/javascript" src="jquery.js"></script>
		<script type="text/javascript" src="kibo.js"></script>
        
	</head>
	
	<body>
    	
    
		<h1> PROJECT TALOS </h1>
		<!-- Key press scripts -->
        
		<script>
		
		var w = new Kibo();
		
		var firedw = false;
		
		w.down(['w'], function() {
		if (!firedw){
		firedw = true;
		console.log('w key pressed');
		$(document).ready(function(){
		
			$("#function").load("function/wInsert.php");
		});}
		}).up('w', function() {
		firedw = false;
		console.log('W Key released');
		
		$(document).ready(function(){
		
			$("#function").load("function/wRelease.php");
		});
		if(!firedw + !fireds + !fireda + !firedd + !firedspace){
			$(document).ready(function(){
		
			$("#function").load("function/Idle.php");
		});
		}
		});
			
		
		
		var s = new Kibo();
		
		var fireds = false;
		
		s.down(['s'], function() {
		if (!fireds) {
		fireds = true;
		console.log('s key pressed');
		$(document).ready(function(){
		
			$("#function").load("function/sInsert.php");
		});}
		}).up('s', function() {
		fireds = false;
		console.log('s Key released');
		$(document).ready(function(){
		
			$("#function").load("function/sRelease.php");
		});
		if(!firedw + !fireds + !fireda + !firedd + !firedspace){
			$(document).ready(function(){
		
			$("#function").load("function/Idle.php");
		});
		}
		});
			
		
		var a = new Kibo();
		
		fireda = false;
		
		a.down(['a'], function() {
		if(!fireda){
		fireda = true;
		console.log('a key pressed');
		
		$(document).ready(function(){
		
			$("#function").load("function/aInsert.php");
		});}
		}).up('a', function() {
		fireda = false;
		console.log('a Key released');
		$(document).ready(function(){
		
			$("#function").load("function/aRelease.php");
		});
		});
		
		
		
		var space = new Kibo();
		
		var firedspace = false;
		
		space.down(['space'], function() {
		if (!firedspace){
		firedspace = true;
		console.log('BRAKE');
		$(document).ready(function(){
		
			$("#function").load("function/brakeInsert.php");
		});}
		}).up('space', function() {
		firedspace = false;
		console.log('BRAKE OFF');
		$(document).ready(function(){
		$("#function").load("function/Idle.php");
		});
		if(!firedw + !fireds + !fireda + !firedd + !firedspace){
			$(document).ready(function(){
		
			$("#function").load("function/Idle.php");
		});
		}
		});
			
		
		
		var d = new Kibo();
		
		firedd = false;
		
		d.down(['d'], function() {
		if(!firedd){
		firedd = true;
		console.log('d key pressed');
		
		$(document).ready(function(){
		
			$("#function").load("function/dInsert.php");
		});}
		}).up('d', function() {
		firedd = false;
		console.log('d Key released');
		$(document).ready(function(){
		
			$("#function").load("function/dRelease.php");
		});
		});
		
		
		</script>
		<!-- Key press scripts finish -->
		
		<div class="main">
		</div>
		
		<div class="top" onMouseDown="forwardON()" onMouseUp="forwardOFF()">
         
   		</div>
		<script>
		function forwardON(){$(document).ready(function(){$("#function").load("function/wInsert.php");});console.log('fwd button 		pressed')};function forwardOFF(){$(document).ready(function(){$("#function").load("function/wRelease.php");});console.log('fwd button released')};
		
		function backON(){$(document).ready(function(){$("#function").load("function/sInsert.php");});console.log('bck button 		pressed')};function backOFF(){$(document).ready(function(){$("#function").load("function/sRelease.php");});console.log('bck button released')};
		
		function leftON(){$(document).ready(function(){$("#function").load("function/aInsert.php");});console.log('lft button 		pressed')};function leftOFF(){$(document).ready(function(){$("#function").load("function/aRelease.php");});console.log('lft button released')};
		
		function rightON(){$(document).ready(function(){$("#function").load("function/dInsert.php");});console.log('rht button 		pressed')};function rightOFF(){$(document).ready(function(){$("#function").load("function/dRelease.php");});console.log('rht button released')};
        </script>
		<section id= "bottom" >
			<div class="bottomLeft" onMouseDown="leftON()" onMouseUp="leftOFF()">
            
			</div>
				
			<div class="bottomMiddle" onMouseDown="backON()" onMouseUp="backOFF()">
           
			</div>
		
			<div class="bottomRight" onMouseDown="rightON()" onMouseUp="rightOFF()">
            
			</div>
		</section>
        
		<div id="function"></div>
        
	</body>
</html>
