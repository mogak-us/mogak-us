<script setup>
import { Icon } from '@iconify/vue';

defineProps({
  workspace: {
    type: Object,
    required: true,
    validator: (obj) => 'id' in obj && 'name' in obj,
  },
});
</script>
<template>
  <div class="w-60 bg-amber-300 border-r-amber-800 border-r-2 h-screen">
    <div class="p-4 w-full aspect-square">
      <h3>{{ workspace.name }}</h3>
      <p>ID: {{ workspace.id }}</p>
    </div>
    <ul class="list-none mx-4">
      <li class="border-b border-amber-700">
        <a :href='`/workspaces/${workspace.id}/meetups`' class=" py-4 flex items-center gap-x-2">
          <Icon icon="material-symbols:group" />
          Meetups
        </a>
      </li>
      <li class="border-b border-amber-700">
        <a :href='`/workspaces/${workspace.id}/members`' class="flex py-4 items-center gap-x-2">
          <Icon icon="material-symbols:group" />
          Members
        </a>
      </li>
      <li>
        <a :href='`/workspaces/${workspace.id}/settings`' class="flex py-4 items-center gap-x-2">
          <Icon icon="material-symbols:settings" />
          Settings
        </a>
      </li>
    </ul>
  </div>
</template>
