<script>
	import SpeechCard from './SpeechCard.svelte';
	import TopicAccordion from './TopicAccordion.svelte';

	let test = [1, 2, 3, 4, 5, 6, 7, 8, 9];
</script>
<div class="py-4 space-y-2">
    {#each test as item}
    <TopicAccordion/>
    {/each}
</div>
