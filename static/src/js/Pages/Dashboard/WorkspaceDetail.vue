<script setup>
import axios from 'axios';

import WorkspaceLayout from '@/layouts/WorkspaceLayout.vue';
import MeetupItem from '@/Components/MeetupItem.vue';
import { ref } from 'vue';

const props =
  defineProps({
    workspace: {
      type: Object,
      required: true,
      validator: (obj) => 'id' in obj && 'name' in obj,
    },
    meetups: {
      type: Array,
      required: true,
      validator: (arr) => arr.every((obj) => 'id' in obj && 'name' in obj && 'date' in obj),
    },
  });

const memberNames = ref([]);

const addMembers = () => {
  const names = memberNames.value
  axios.post(`/workspaces/${props.workspace.id}/add_members/`, { member_names: names })
    .then((response) => {
      console.log(response.data);
    })
    .catch((error) => {
      console.error(error);
    });
}

</script>

<template>
  <WorkspaceLayout :workspace="workspace">
    <div>
      <h2>Meetups</h2>
      <div class="flex flex-col gap-y-4">
        <MeetupItem v-for="meetup in meetups" :key="meetup.id" :workspace="workspace" :meetup="meetup" />
      </div>
    </div>

    {/* Add Members using dynamic input */}
    <div>
      <h2>Members</h2>
      <div class="flex flex-col gap-y-4">
        <div v-for="(name, index) in memberNames" :key="index">
          <input v-model="memberNames[index]" />
          <button @click="memberNames.splice(index, 1)">Remove</button>
        </div>
        <button @click="memberNames.push('')">Add Member</button>
      </div>
      <button @click="addMembers">Add Members</button>
    </div>

  </WorkspaceLayout>
</template>
