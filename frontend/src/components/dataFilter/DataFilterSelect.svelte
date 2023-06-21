<script>
	export let selectedValue = null;
	export let values = [];
    export let tooltipText = '';
    export let labelText = '';
</script>

<div class="relative">
	<label class="block text-gray-700 text-sm font-bold mb-2 basis-2/3" for="legislatur"
		>{labelText}:</label
	>
	<div
		class="tooltip tooltip-left absolute top-0 right-0"
		data-tip={tooltipText}
	>
		<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="w-5 h-5">
			<path
				fill-rule="evenodd"
				d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a.75.75 0 000 1.5h.253a.25.25 0 01.244.304l-.459 2.066A1.75 1.75 0 0010.747 15H11a.75.75 0 000-1.5h-.253a.25.25 0 01-.244-.304l.459-2.066A1.75 1.75 0 009.253 9H9z"
				clip-rule="evenodd"
			/>
		</svg>
	</div>
	<select
		class="select select-bordered w-full basis-1"
		bind:value={selectedValue}
		name={labelText}
		id="legislatur"
	>
		{#each values as item}
			<option value={item}>{item}</option>
		{/each}
	</select>
</div>
