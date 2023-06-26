<script>
	import SpeechCard from './SpeechCard.svelte';

	let test = [1, 2, 3, 4, 5, 6, 7, 8, 9];
</script>

<div class="collapse collapse-arrow bg-base-200">
	<input type="radio" name="my-accordion-2" checked="checked" />
	<div class="collapse-title text-xl font-medium">TOP test</div>
	<div class="collapse-content">
		<div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 2xl:grid-cols-4 gap-4 py-4">
			{#each test as item}
				<SpeechCard />
			{/each}
		</div>
	</div>
</div>
