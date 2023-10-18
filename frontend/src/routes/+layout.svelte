<script>
	import '../app.css';
	import Footer from './footer.svelte'
</script>

<div class="flex flex-col h-screen justify-between">
	<div class="navbar bg-base-100 shadow-sm">
		<div class="navbar-start">
			<div class="dropdown">
				<label tabindex="0" class="btn btn-ghost lg:hidden">
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-5 w-5"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
						><path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M4 6h16M4 12h8m-8 6h16"
						/></svg
					>
				</label>
				<ul
					tabindex="0"
					class="menu menu-compact dropdown-content mt-3 p-2 shadow bg-base-100 rounded-box w-52"
				>
					<li><a href="/wortmeldungsarten">Wortmeldungsarten</a></li>
					<li><a href="/wortmeldungsdauer">Wortmeldungsdauer</a></li>		
					<li><a href="/wortmeldungsverhältnisse">Wortmeldungsverhältnis</a></li>			
				</ul>
			</div>
			<a class="btn btn-ghost normal-case text-xl" href="/">parli-info.org</a>
		</div>

		<div class="navbar-center hidden lg:flex">
			<ul class="menu menu-horizontal px-1">
				<li><a href="/wortmeldungsarten">Wortmeldungsarten</a></li>	
				<li><a href="/wortmeldungsdauer">Wortmeldungsdauer</a></li>		
				<li><a href="/wortmeldungsverhältnisse">Wortmeldungsverhältnis</a></li>			
			</ul>
		</div>
		<div class="navbar-end">
		</div>
	</div>

	<div class="mb-auto container sm:px-6 px-3 sm:min-w-fit min-w-full self-center">
		<slot />
	</div>
	
	<Footer class="self-end"></Footer>
</div>

