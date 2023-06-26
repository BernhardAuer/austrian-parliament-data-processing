<script>
	import TopicAccordion from './TopicAccordion.svelte';
	import SpeechService from './../../services/speechService.js';
	import { onMount } from 'svelte';
	let service = new SpeechService();
	let speeches = [];
	let speechesByTopic = [];
    let topics = [];
    const getLongNameOfPoliticalParty = (shortName) => {
        let mapDict = {
			"v": "ÖVP",
			"s": "SPÖ",
			"f": "FPÖ",
			"g": "GRÜNE",
			"n": "NEOS",
		}
		let abbrToLower = shortName.toLowerCase();
		return mapDict[abbrToLower];
    }
	const groupBy = (x, f) => x.reduce((a, b, i) => ((a[f(b, i, x)] ||= []).push(b), a), {}); // credit: https://stackoverflow.com/questions/14446511/most-efficient-method-to-groupby-on-an-array-of-objects
	onMount(async () => {
		speeches = await service.fetchSpeeches({ legislature: 'XXVII', meetingNumber: 217 });
        speeches = speeches.map(x => {return {...x, politicalPartie: getLongNameOfPoliticalParty(x.politicalPartie)}});
		speechesByTopic = groupBy(speeches, (x) => x.topic);

		console.log(speechesByTopic);

		topics = Object.keys(speechesByTopic);
		console.log(topics);
        topics.forEach((key, index) => {
            console.log(`${key}: ${speechesByTopic[key][0].nameOfSpeaker}`);
        });
	});
</script>

<div class="py-4 space-y-2">
	{#each topics as topic}
		<TopicAccordion {topic} topNr={speechesByTopic[topic][0]?.topNr} speeches={speechesByTopic[topic]} />
	{/each}
</div>
