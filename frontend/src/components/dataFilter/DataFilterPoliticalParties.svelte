<script>
	export let selectedPoliticalParties = [];
	export let politicalParties = [
		{ shortName: 'V', longName: 'ÖVP' },
		{ shortName: 'S', longName: 'SPÖ' },
		{ shortName: 'F', longName: 'FPÖ' },
		{ shortName: 'G', longName: 'GRÜNE' },
		{ shortName: 'N', longName: 'NEOS' }
	];
	export let tooltipText = '';
	export let labelText = '';
</script>

<div class="relative">
	<label class="block text-gray-700 text-sm font-bold mb-2" for="politicalParty">{labelText}:</label>
	<div class="tooltip tooltip-left absolute top-0 right-0" data-tip={tooltipText}>
		<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="w-5 h-5">
			<path
				fill-rule="evenodd"
				d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a.75.75 0 000 1.5h.253a.25.25 0 01.244.304l-.459 2.066A1.75 1.75 0 0010.747 15H11a.75.75 0 000-1.5h-.253a.25.25 0 01-.244-.304l.459-2.066A1.75 1.75 0 009.253 9H9z"
				clip-rule="evenodd"
			/>
		</svg>
	</div>
	<div class="grid grid-cols-3 gap-2">
		{#each politicalParties as item}
			<div class="flex flex-row gap-2 border-2 rounded-full items-center">
				<input
					type="checkbox"
					class="checkbox"
					id="id-{item.shortName}"
					bind:group={selectedPoliticalParties}
					name={item.longName}
					value={item.shortName}
				/>
				<label for="id-{item.shortName}">{item.longName}</label>
			</div>
		{/each}
	</div>
</div>
