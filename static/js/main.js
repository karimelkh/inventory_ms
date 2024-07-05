$(document).ready(function()
{
	$("#hide-sidebar-btn").click(hideSideBar);
	$("#show-sidebar-btn").click(showSideBar);
});

function hideSideBar()
{
	$("#sidebar").hide();
	$("#main-sec").removeClass("grid");
	$("#show-sidebar-btn").removeClass("hidden");
}

function showSideBar()
{
	$("#show-sidebar-btn").addClass("hidden");
	$("#main-sec").addClass("grid");
	$("#sidebar").show();
}
