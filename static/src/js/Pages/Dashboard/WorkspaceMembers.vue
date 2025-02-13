<script setup lang="ts">
import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table'

import { ref, onMounted, defineProps, reactive } from 'vue'
import axios from 'axios'

import WorkspaceLayout from '@/layouts/WorkspaceLayout.vue'

const props = defineProps({
  workspace: {
    type: Object,
    required: true,
    validator: (obj) => 'id' in obj && 'name' in obj,
  },
})

const members = ref([])

onMounted(async () => {
  const response = await axios.get(`/api/workspaces/${props.workspace.id}/members/`)
  members.value = response.data
})
const newMember = reactive({
  name: '',
})

const addMember = async () => {
  if (newMember.name.trim() === '') return

  try {
    await axios.post(`/api/workspaces/${props.workspace.id}/members/`, {
      member_names: [newMember.name],
    })
    members.value.push({ id: null, alias_name: newMember.name })
    newMember.name = ''
  } catch (error) {
    console.error('Failed to add member:', error)
  }
}
</script>

<template>
  <WorkspaceLayout :workspace="workspace">
    <div class="bg-white shadow-md rounded my-6 p-4">
      <form @submit.prevent="addMember" class="mb-4">
        <input v-model="newMember.name" type="text" placeholder="Enter member name"
          class="border rounded py-2 px-3 text-gray-700" />
        <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded ml-2">
          Add Member
        </button>
      </form>
      <Table class="min-w-full bg-white">
        <TableCaption class="text-lg font-semibold py-4">Workspace Members</TableCaption>
        <TableHeader>
          <TableRow class="bg-gray-200 text-gray-600 uppercase text-sm leading-normal">
            <TableHead class="py-3 px-6 text-left">ID</TableHead>
            <TableHead class="py-3 px-6 text-left">Alias Name</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody class="text-gray-600 text-sm font-light">
          <TableRow v-for="member in members" :key="member.id" class="border-b border-gray-200 hover:bg-blue-50">
            <TableCell class="py-3 px-6 text-left whitespace-nowrap font-medium">{{ member.id }}</TableCell>
            <TableCell class="py-3 px-6 text-left">{{ member.alias_name }}</TableCell>
          </TableRow>
        </TableBody>
      </Table>
    </div>
  </WorkspaceLayout>
</template>
