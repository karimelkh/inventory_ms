$(document).ready(function()
{
	$("#theme-switcher").click(switchTheme);
});

function switchTheme()
{
	$("html").toggleClass("dark");
	$("#light-icon").toggle();
	$("#dark-icon").toggle();
}
