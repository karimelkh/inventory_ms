$(document).ready(function()
{
	$("#tog-usermenu").click(toggleUserMenu);
	$("#tog-newmenu").click(toggleNewMenu);
	$("#tog-browsemenu").click(toggleBrowseMenu);
});

function toggleUserMenu()
{
	$("#usermenu").toggle();
}

function toggleNewMenu()
{
	$("#newmenu").toggle();
}

function toggleBrowseMenu()
{
	$("#browsemenu").toggle();
}

