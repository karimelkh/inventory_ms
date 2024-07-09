$(document).ready(function()
{
	$("#hs-pw-btn").click(togglePW);
});

function togglePW()
{
	let pwf = $("#password");
	let tglPWBtn = $("#hs-pw-btn");

	if(pwf.hasClass("hided-pw-field")) {
		pwf.removeClass("hided-pw-field");
		pwf.addClass("shown-pw-field");
		pwf.prop("type", "text");
		tglPWBtn.addClass("fa-eye-slash");
		tglPWBtn.removeClass("fa-eye");
	}
	else {
		pwf.removeClass("shown-pw-field");
		pwf.addClass("hided-pw-field");
		pwf.prop("type", "password");
		tglPWBtn.addClass("fa-eye");
		tglPWBtn.removeClass("fa-eye-slash");
	}
}
