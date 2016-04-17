# Combined from the source
enc = "6f645f6164736d6f645f79616369766573695f656c6e6f5f73755f796c7566655f66695f72657665656e6f796f6e6b5f615f737774756f620a74695f"

flag = ""

for x in range(0, len(enc), 8):
    group = enc[x:x+8]
    tmp = ""
    for y in range(0, len(group), 2):
        tmp = chr(int(group[y:y+2], 16)) + tmp
    flag += tmp

print flag

# a_doomsday_device_is_only_useful_if_everyone_knows_about_it
