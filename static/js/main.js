$(document).ready(function()
{
	$("#hide-sidebar-btn").click(hideSideBar);
	$("#show-sidebar-btn").click(showSideBar);
	$("#tog-usermenu-btn").click(toggleUserMenu);
	$("#tog-newmenu-btn").click(toggleNewMenu);
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

function toggleUserMenu()
{
	$("#usermenu-list").toggle();
}

function toggleNewMenu()
{
	$("#newmenu-list").toggle();
}
