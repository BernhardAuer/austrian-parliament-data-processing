import { error } from '@sveltejs/kit';
import SpeechService from './../../../../services/speechService.js';
let service = new SpeechService();
let speechesByTopic = [];
let topics = [];
const groupBy = (x, f) => x.reduce((a, b, i) => ((a[f(b, i, x)] ||= []).push(b), a), {}); // credit: https://stackoverflow.com/questions/14446511/most-efficient-method-to-groupby-on-an-array-of-objects

/** @type {import('./$types').PageLoad} */
export async function load({ params, url }) {
    let speeches = await service.fetchSpeeches({ legislature: params.legislature, meetingNumber: params.meetingNumber });    
    if (Array.isArray(speeches) && !speeches.length) {
        throw error(404, 'Not found');
    }

    // sort alphanumeric (topNr can be "Top 2-4", "Top 1" or null for example)
    speeches.sort((a,b) => new Intl.Collator('de',{numeric:true, sensitivity:'accent'}).compare(a.topNr,b.topNr));

    speechesByTopic = groupBy(speeches, (x) => x.topic);
    topics = Object.keys(speechesByTopic);
    return {
        topics: topics,
        speechesByTopic: speechesByTopic,
        legislature: params.legislature,
        meetingNr: params.meetingNumber,
        selectedTopicUrlSlug: url.searchParams.get('thema')
    };
}
