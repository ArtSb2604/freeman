$( document ).ready(function() {
	$(".hamburger").click(function(){
		$(this).toggleClass("is-active");
		$("#menu").toggleClass("hidden");
		$("body").toggleClass("fixed");
		
		$(".dropdown").children("ul").slideUp(250);
		$(".dropdown").removeClass("opened")
	});
	$(".dropdown").click(function(){
		$(this).children("ul").slideToggle(250);
		$(this).toggleClass("opened");
		$(".dropdown").not(this).children("ul").slideUp(250);
		$(".dropdown").not(this).removeClass("opened")
	});

	// popup login, registration, restore password
	$(".logIn__btn").click(function(){
		$(".popup-logIn").fadeIn(250);
		$("body").addClass("fixed");
		$(".popup").not(".popup-logIn").fadeOut(250);
	});
	$(".reg__btn").click(function(){
		$(".popup-reg").fadeIn(250);
		$("body").addClass("fixed");
		$(".popup").not(".popup-reg").fadeOut(250);
	});
	$(".restore__btn").click(function(){
		$(".popup-restore").fadeIn(250);
		$("body").addClass("fixed");
		$(".popup").not(".popup-restore").fadeOut(250);
	});
	$(".popup-close__btn").click(function(){
		$(this).parents(".popup").fadeOut(250);
		$("body").removeClass("fixed");
	})
	$(".popup").click(function(e){
		if(!$(".popup-content").is(e.target) && $(".popup-content").has(e.target).length === 0){
			$(this).fadeOut(250);
			$("body").removeClass("fixed");
		}
	});

	$(".popup-reg__btn__switchOn").click(function(){
		$(".popup-reg__form-switchable").slideDown(250);
		$(this).addClass("active");
		$(".popup-reg__btn__switchOff").removeClass("active")
	});
	$(".popup-reg__btn__switchOff").click(function(){
		$(".popup-reg__form-switchable").slideUp(250);
		$(this).addClass("active");
		$(".popup-reg__btn__switchOn").removeClass("active")
	});
});