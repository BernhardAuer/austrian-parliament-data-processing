<script>
	import '../app.css';
	import Footer from './footer.svelte'
	import { fade } from "svelte/transition";
  	import { navigating } from "$app/stores";
	import { BarLoader } from 'svelte-loading-spinners';
	import { page } from '$app/stores';

	const legislature = $page.params['legislature'];
	const meetingNumber = $page.params['meetingNumber'];
	const topic = $page.params['topic'];

	const getDataFilterUrlParams = () => {
		let resultParams = "";
		if (legislature != undefined && meetingNumber != undefined) {
			resultParams += `/${legislature}/${meetingNumber}`;
		}
		if (topic != undefined) {
			resultParams += `/${topic}`;
		}
		return resultParams;
	};
	$: legislature, meetingNumber, topic, console.log(getDataFilterUrlParams());
	$: $page, console.log(JSON.stringify($page.params))
</script>

<!-- shoutout to https://www.ratamero.com/blog/showing-a-loading-spinner-when-navigation-is-delayed-in-sveltekit -->
{#if Boolean($navigating)}
	<div class="css-tweaked-bar-loader w-full fixed top-0 z-50">
		<BarLoader size="60" color="#1e40af" duration="1s"/>
	</div>
	<div class="fixed w-full h-full z-10" in:fade={{ duration: 150 }}>
		<div class="absolute w-full h-full bg-white dark:bg-cyan-800 opacity-50 z-10"></div>
	</div>
{/if}

<div class="flex flex-col h-screen justify-between">
	<div class="navbar bg-base-100 shadow-sm">
		<div class="navbar-start">
			<div class="dropdown">
				<label tabindex="0" role="button" class="btn btn-ghost lg:hidden">
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-5 w-5"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor">
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M4 6h16M4 12h8m-8 6h16"/>
					</svg>
				</label>
				<ul
					tabindex="0"
					class="menu menu-compact dropdown-content z-[10] mt-3 p-2 shadow bg-base-100 rounded-box w-52"
				>
					<li><a href="/wortmeldungsarten">Wortmeldungsarten</a></li>
					<li><a href="/wortmeldungsdauer">Wortmeldungsdauer</a></li>		
					<li><a href="/wortmeldungsverhältnisse">Wortmeldungsverhältnis</a></li>		
					<li><a href="/sitzungsverteilung">Nationalratssitzungen</a></li>			
				</ul>
			</div>
			<a class="btn btn-ghost normal-case text-xl" href="/">parli-info.org</a>
		</div>

		<div class="navbar-center hidden lg:flex">
			<ul class="menu menu-horizontal px-1">
				<li><a href={"/wortmeldungsarten" + getDataFilterUrlParams()}>Wortmeldungsarten</a></li>	
				<li><a href={"/wortmeldungsdauer" + getDataFilterUrlParams()}>Wortmeldungsdauer</a></li>		
				<li><a href={"/wortmeldungsverhältnisse" + getDataFilterUrlParams()}>Wortmeldungsverhältnis</a></li>		
				<li><a href={"/sitzungsverteilung" + getDataFilterUrlParams()}>Nationalratssitzungen</a></li>				
			</ul>
		</div>
		<div class="navbar-end">
		</div>
	</div>

	<div class="mb-auto max-sm:container sm:px-6 px-3 self-center">
		<slot />
	</div>
	
	<Footer class="self-end"></Footer>
</div>

<style>
	/* overwrite svelte component styling from svelte-loading-spinners */
	.css-tweaked-bar-loader :global(.wrapper) {  /* this is needed so css is not leaking ... see https://stackoverflow.com/a/56989664  */
		width: 100% !important;
	}
</style>